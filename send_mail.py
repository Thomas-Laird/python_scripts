import smtplib
import getpass


client = smtplib.SMTP('smtp.gmail.com')
client.starttls()

client.login('tomlaird1@gmail.com', 'pfjswjiqpqfifhxs')

res = client.sendmail('tomlaird1@gmail.com', 'tomlaird1@gmail.com', 'Subject: Python test.\nIt worked yet again!')
print(res)
client.quit()


