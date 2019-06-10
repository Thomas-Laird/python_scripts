import sqlalchemy
import getpass


endpoint = input("Database server endpoint: ")
name = input('Name: ')
password = getpass.getpass()

engine = sqlalchemy.create_engine("postgresql://"+name+":"+password+"@"+endpoint, echo=True)

