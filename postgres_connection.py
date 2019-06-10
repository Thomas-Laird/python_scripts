import sqlalchemy
import getpass

name = input('Name: ')
password = getpass.getpass()

engine = sqlalchemy.create_engine("postgresql://"+name+":"+password+"@laird-postgres.cbhozu8gpff2.eu-west-1.rds.amazonaws.com:5432/laird_db", echo=True)

