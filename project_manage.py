# import database module
import csv, database
from database import *

# define a funcion called initializing

_database = DB()

def initializing():
    """
    here are things to do in this function:
    - create an object to read all csv files that will serve as a persistent state for this program
    - create an object to read all csv files that will serve as a persistent state for this program
    - create all the corresponding tables for those csv files
    - see the guide how many tables are needed
    - add all these tables to the database
    """
    # csv_reader = ReadCsv('persons.csv')
    # csv_reader.data

    read_person = ReadCsv('persons.csv')
    person_table = Table('Person table', read_person.data)
    _database.insert(person_table)

    # print(person_table)

    read_login = ReadCsv('login.csv')
    login_table = Table('Login table', read_login.data)
    _database.insert(login_table)

    # print(login_table)

    project_data = [
        {'ProjectID': None, 'Title': None, 'Lead': None, 'Member1': None,
         'Member2': None, 'Advisor': None, 'Status': None}]
    project_table = Table('Project table', project_data)
    _database.insert(project_table)

    # print(project_table)

    adPendReq_data = [
        {'ProjectID': None, 'to_be_advisor': None, 'Response': None, 'Response_date': None}]
    adPendReq_table = Table('Advisor_pending_request table', adPendReq_data)
    _database.insert(adPendReq_table)

    # print(advisor_pending_request_table)

    memPendReq_data = [{'ProjectID': None, 'to_be_member': None, 'Response': None, 'Response_date': None}]
    memPendReq_table = Table('Member_pending_request table', memPendReq_data)
    _database.insert(memPendReq_table)

    # print(memPendReq_table)
    #
    # print(_database.table_name())  # check all table in database


# define a function called login

def login():
    """
    here are things to do in this function:
    - add code that performs a login task
    - ask a user for a username and password
    - returns [ID, role] if valid, otherwise returning None
    """
    while True:
        username = input("Enter username: ")

        # Search for the username in the login table
        login_table = _database.search('Login table')

        user_found = None
        for user in login_table.table:
            if user['username'] == username:
                user_found = user
                break

        if user_found:
            break
        else:
            print("Username not found. Please try again.")

    # Once a valid username is found, ask for the password
    password = input("Enter password: ")
    if user_found['password'] == password:
        return [user_found['ID'], user_found['role']]

    else:
        return None


# define a function called exit


def exit():
    """
    here are things to do in this function:
    - write out all the tables that have been modified to the corresponding csv files
    - By now, you know how to read in a csv file and transform it into a list of dictionaries.
        For this project, you also need to know how to do the reverse,
        i.e., writing out to a csv file given a list of dictionaries.
        See the link below for a tutorial on how to do this:
        https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python
    """
    for table in _database.database:
        filename = table.table_name + '.csv'

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            if table.table:
                headers = table.table[0].keys()

                writer = csv.DictWriter(file, fieldnames=headers)

                writer.writeheader()
                writer.writerows(table.table)
            else:
                print(f"Table '{table.table_name}' is empty. No CSV file created.")

    print("All tables have been written out to CSV files.")


# make calls to the initializing and login functions defined above

initializing()
val = login()

""" based on the return value for login, activate the code that 
performs activities according to the role defined for that person_id """

class Student:
    def __init__(self):
        self.
# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
