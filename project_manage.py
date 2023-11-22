# import database module
import csv
from database import *

# define a funcion called initializing

# PMdatabase = database.DB()
PMdatabase = DB()


def initializing():
    read_person = CSVReader('persons.csv')
    CSVReader.read_csv(read_person)
    persons_table = Table('persons', read_person.data)
    PMdatabase.insert(persons_table)

    read_login = CSVReader('login.csv')
    CSVReader.read_csv(read_login)
    user_table = Table('login', read_login.data)  # dict in list
    PMdatabase.insert(user_table)


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a funcion called login

def login():
    ask_username = input('Enter username: ')
    ask_password = input('Enter password: ')
    search_login = PMdatabase.search('login')

    # print(search_login)
    for i in search_login.table:
        if ask_username == i['username'] and ask_password == i['password']:
            return [i['ID'], i['role']]
    return None
    # # print(login_table['ID'])
    # print(check_login)


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
# def exit():
#     for table in PMdatabase.database:
#         table_name = table.table_name
#         # print(table)
#         with open(os.path.join(table.__location__, f'{table_name}.csv'), 'w', newline='') as file:
#             writer = csv.DictWriter(file, fieldnames=table.table[0].keys())
#             writer.writeheader()
#             writer.writerows(table.table)


def exit():
    for table in PMdatabase.database:
        table_name = table.table_name
        with open(os.path.join(table.__location__, f'{table_name}.csv'), 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=table.table[0].keys())
            writer.writeheader()
            writer.writerows(table.table)
    # person_file = open('persons.csv', 'w', newline='')
    # persons_writer = csv.DictWriter(person_file, ['ID', 'fist', 'last', 'type'])
    # persons_writer.writeheader()
    # persons_writer.writerows(PMdatabase.search('persons').table)
    #
    # login_file = open('login.csv', 'w', newline='')
    # login_writer = csv.DictWriter(login_file, ['ID', 'username', 'password', 'role'])
    # login_writer.writeheader()
    # login_writer.writerows(PMdatabase.search('login').table)
    #
    # person_file.close()
    # login_file.close()

# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
# print(PMdatabase.search('persons'))
# print(PMdatabase.search('login'))
# print(type(PMdatabase))

val = login()
print(val)  # login


# print(val)
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

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

# once everyhthing is done, make a call to the exit function
exit()
