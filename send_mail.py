import smtplib
import getpass


email = input("Input email to use for test: ")
password = getpass.getpass()

client = smtplib.SMTP('smtp.gmail.com')
client.starttls()

client.login(email, password)

res = client.sendmail(email, email, 'Subject: Python test.\nThis email was sent using python!')
print(res)
client.quit()


