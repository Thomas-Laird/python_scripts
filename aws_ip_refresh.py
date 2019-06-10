import urllib3
import boto3
from botocore.exceptions import ParamValidationError

# Retrieve current machine public Ip from an api website.

try:
    ip_api_url = "https://api.ipify.org/"
    http = urllib3.PoolManager()
    res = http.request("GET", ip_api_url)
    new_ip_cidr = res.data.decode('utf-8')+'/32'
except urllib3.exceptions.NewConnectionError:
    print('could not connect to website')


description = 'Home'


def find_old_ip(security_group_rule_list):
    for rule in security_group_rule_list:
        if rule.get('Description') == description:
            return rule.get('CidrIp')


# Connect to aws and retrieve the desired security group.
ec2 = boto3.client('ec2')
default_security_group = ec2.describe_security_groups(GroupNames=['default']).get('SecurityGroups')[0]


# Attempt to revoke the ingress rule associated with the old ip.
try:
    old_ip_cidr = find_old_ip(default_security_group.get('IpPermissions')[0].get('IpRanges'))
    revoke_response = ec2.revoke_security_group_ingress(GroupId=default_security_group.get('GroupId'), IpPermissions=[
        {'FromPort': -1, 'IpProtocol': '-1', 'IpRanges': [{'CidrIp': old_ip_cidr, 'Description': description}]}])
    print(old_ip_cidr)
except ParamValidationError:
    print('Could not find rule for IP: ',old_ip_cidr)


print(new_ip_cidr)

authorize_response = ec2.authorize_security_group_ingress(GroupId=default_security_group.get('GroupId'), IpPermissions=[{'FromPort': -1, 'IpProtocol': '-1', 'IpRanges': [{'CidrIp': new_ip_cidr, 'Description': description}]}])