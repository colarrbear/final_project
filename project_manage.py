# import database module
import csv, database
from database import *
import random
# define a funcion called initializing

_database = DB()


def generate_random_project_id():
    """
    Generates a random 4-digit ID for a project.
    Returns a string of 4 digits.
    """
    __random_project_id = f"{random.randint(0, 9999):04d}"
    return __random_project_id


random_project_id = generate_random_project_id()


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
    person_table = Table('persons', read_person.data)
    _database.insert(person_table)

    # print(person_table)

    read_login = ReadCsv('login.csv')
    login_table = Table('login', read_login.data)
    _database.insert(login_table)

    # print(login_table)

    # project_data = [
    #     {'ProjectID': None, 'Title': None, 'Lead': None, 'Member1': None,
    #      'Member2': None, 'Advisor': None, 'Status': None}
    # ]
    project_data = [
        {'ProjectID': random_project_id, 'Title': None, 'Lead': None, 'Member1': None,
         'Member2': None, 'Advisor': None, 'Status': None}
    ]
    project_table = Table('project', project_data)
    _database.insert(project_table)


    # print(project_table)

    adPendReq_data = [
        {'ProjectID': None, 'to_be_advisor': None, 'Response': None, 'Response_date': None}]
    adPendReq_table = Table('Advisor_pending_request', adPendReq_data)
    _database.insert(adPendReq_table)

    # print(advisor_pending_request_table)

    memPendReq_data = [{'ProjectID': None, 'to_be_member': None, 'Response': None, 'Response_date': None}]
    memPendReq_table = Table('Member_pending_request', memPendReq_data)
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
        __login_table = _database.search('login')

        user_found = None
        for user in __login_table.table:
            if user['username'] == username:
                user_found = user
                break

        if user_found:
            password = input("Enter password: ")
            if user_found['password'] == password:
                __login_table = _database.search('login')
                for person in __login_table.table:
                    if person['ID'] == user_found['ID']:
                        return [user_found['ID'], person['role']]
                return None  # Return None if the ID is not found in the persons table
        return None  # Return None if the username is not found or the password is incorrect

        # user_found = None
        # for user in login_table.table:
        #     if user['username'] == username:
        #         user_found = user
        #         password = input("Enter password: ")
        #         if user_found['password'] == password:
        #             person_table = _database.search('Person table')
        #             for person in person_table.table:
        #                 if person['ID'] == user_found['ID']:
        #                     return [user_found['ID'], person['role']]
        #             return None
        #         break


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
    # for table in _database.database:
    #     filename = table.table_name + '.csv'
    #
    #     with open(filename, mode='w', newline='', encoding='utf-8') as file:
    #         if table.table:
    #             headers = table.table[0].keys()
    #
    #             writer = csv.DictWriter(file, fieldnames=headers)
    #
    #             writer.writeheader()
    #             writer.writerows(table.table)
    #         else:
    #             print(f"Table '{table.table_name}' is empty. No CSV file created.")
    #
    # print("All tables have been written out to CSV files.")
    for table in _database.database:
        filename = table.table_name + '.csv'
        file_exists = os.path.exists(filename)

        if not file_exists:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                if table.table:
                    headers = table.table[0].keys()

                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(table.table)
                else:
                    print(f"Table '{table.table_name}' is empty. No CSV file created.")
        else:
            print(f"CSV file for table '{table.table_name}' already exists. No new file created.")

    print("All tables have been processed for CSV file output.")


# function part
############################################################

class Student:
    def __init__(self, ID, member_pending_request_table, project_table):
        self.ID = ID
        self.memberStatus = self.get_member_status(member_pending_request_table)
        self.projectID = self.get_project_id(project_table)

    def get_member_status(self, member_pending_request):
        for request in member_pending_request.table:
            if request['to_be_member'] == self.ID:
                return request['Response']
        return None

    def get_project_id(self, project_table):
        for project in project_table.table:
            if project['Member1'] == self.ID or project['Member2'] == self.ID:
                return project['ProjectID']
        return None

    def view_requests(self, member_pending_request_table):
        pending_requests = [request for request in
                            member_pending_request_table.table if
                            request['to_be_member'] == self.ID]
        for request in pending_requests:
            print(f"ProjectID: {request['ProjectID']}, Response: {request['Response']}, Date: {request.get('Response_date', 'N/A')}")
        return pending_requests

    def accept_deny_request(self, request_id, accept, member_pending_request_table, project_table):
        for request in member_pending_request_table.table:
            if request['ProjectID'] == request_id:
                if accept:
                    request['Response'] = 'Accepted'
                    for project in project_table.table:
                        if project['ProjectID'] == request_id:
                            if self.ID != project['Member1'] and self.ID != \
                                    project['Member2']:
                                # Assign the student to the first available member slot
                                if project['Member1'] is None:
                                    project['Member1'] = self.ID
                                elif project['Member2'] is None:
                                    project['Member2'] = self.ID
                                else:
                                    print(
                                        "Project already has maximum members.")
                                break
                else:
                    request['Response'] = 'Denied'
                break

    def handle_requests(self, member_pending_request_table, project_table):
        print('Project Invitation:')
        pending_requests = self.view_requests(member_pending_request_table)

        # view_requests(memPendReq_table)
        # self.ID.view_requests(memPendReq_table)

        # print('Project Invites:')
        # for i in range(len(pending_requests)):
        #     print(pending_requests[i])

        if pending_requests:
            # Ask the user to choose a request to respond to
            request_id = input(
                "Enter the ProjectID to respond to (or 'exit' to cancel): ")
            if request_id.lower() == 'exit':
                return

            # Ask the user to accept or deny the request
            response = input(
                "Do you want to accept (type 'accept') or deny (type 'deny') the request? ")
            if response.lower() in ['accept', 'deny']:
                accept = response.lower() == 'accept'
                self.accept_deny_request(request_id, accept,
                                         member_pending_request_table,
                                         project_table)
                print("Request response updated.")
            else:
                print("Invalid response. No action taken.")
        else:
            print("No pending requests.")

    def change_to_lead(self, project_id, login_table, member_pending_request_table, project_table):
        """
        Change the role to 'lead' for a project. Update project_table and login table.
        Must deny all member requests before changing the role.
        """
        # Implementation details will vary based on how roles and requests are handled

        # Deny all pending member requests for the specified project
        for request in member_pending_request_table.table:
            if request['to_be_member'] == self.ID:
                request['Response'] = 'Denied'

        # # Check if the project exists, and if not, create a new one
        # project_found = False
        # for project in project_table.table:
        #     if project['ProjectID'] == project_id:
        #         project_found = True
        #         break

        # Check if this student is already a lead in any project
        is_already_lead = any(
            project['Lead'] == self.ID for project in project_table.table)

        if is_already_lead:
            # If already a lead, display the project details
            print("This student is already a project lead.")
            for project in project_table.table:
                if project['Lead'] == self.ID:
                    self.view_project_details(project['ProjectID'],
                                              project_table)
        else:
            # If not a lead, create or update a project
            project_found = False
            for project in project_table.table:
                if project['ProjectID'] == project_id:
                    project['Lead'] = self.ID
                    project_found = True
                    break

            if not project_found:
                new_project = {'ProjectID': project_id, 'Title': 'New Project',
                               'Lead': self.ID, 'Member1': None,
                               'Member2': None, 'Advisor': None,
                               'Status': 'Active'}
                project_table.insert(new_project)

            # Update the login table
            for user in login_table.table:
                if user['ID'] == self.ID:
                    user['role'] = 'lead'
                    break

        # for project in project_table.table:
        #     if project['Lead'] == self.ID and project['ProjectID'] != project_id:
        #         print(
        #             f"Cannot assign lead role for {project_id}. Student is already a lead in Project {project['ProjectID']}.")
        #         return
        #
        # if not project_found:
        #     # Create a new project
        #     new_project = {'ProjectID': project_id, 'Title': 'New Project', 'Lead': self.ID, 'Member1': None, 'Member2': None, 'Advisor': None, 'Status': 'Active'}
        #     project_table.insert(new_project)
        # else:
        #     # Update the existing project to set this student as the lead
        #     for project in project_table.table:
        #         if project['ProjectID'] == project_id:
        #             project['Lead'] = self.ID
        #             break
        #
        # # Update the login_table to reflect the new role
        # for user in login_table.table:
        #     if user['ID'] == self.ID:
        #         user['role'] = 'lead'
        #         break
        print(f"Role changed to 'lead' for project {project_id}. New project created.")

        # print(f"Role changed to 'lead' for project {project_id}. New project created: {not project_found}")
        # Update the project_table to set this student as the lead
        # project_found = False
        # for project in project_table.table:
        #     if project['ProjectID'] == project_id:
        #         project['Lead'] = self.ID
        #         project_found = True
        #         break
        #
        # if not project_found:
        #     print(f"No project found with ProjectID: {project_id}")
        #     return
        #
        # # Optionally, update the login_table if it stores project roles
        # for user in login_table.table:
        #     if user['ID'] == self.ID:
        #         user['role'] = 'lead'
        #         break
        #
        # print(f"Role changed to 'lead' for project {project_id}.")

#   ทันก็ทำ ไม่ทันก็ลบ
    # def view_project_details(self, project_id, project_table):
    #     """
    #     View project details from the project_table.
    #     """
    #     print('Project: ')
    #     student.view_requests(memPendReq_table)
    #     # Implementation depends on how project details are stored and retrieved
    #     for project in project_table.table:
    #         if project['ProjectID'] == project_id:
    #             # Display the details of the project
    #             print("Project Details:")
    #             for key, value in project.items():
    #                 print(f"{key}: {value}")
    #             return project
    #
    #     # If project is not found
    #     print(f"No project found with ProjectID: {project_id}")
    #     return None


# main part

# def student_menu(Student):
#     while True:
#         print("\n--- Student Menu ---")
#         print("1. View Pending Requests")
#         print("2. Accept or Deny Requests")
#         print("3. View Project Details")
#         print("4. Change Role to Lead")
#         print("5. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == '1':
#             student_instance.view_requests(Member_pending_request)
#         elif choice == '2':
#             student_instance.handle_requests(member_pending_request_table, project_table)
#         elif choice == '3':
#             project_id = input("Enter the Project ID to view details: ")
#             student_instance.view_project_details(project_id, project_table)
#         elif choice == '4':
#             project_id = input("Enter the Project ID to change role to lead: ")
#             student_instance.change_to_lead(project_id, login_table, member_pending_request_table, project_table)
#         elif choice == '5':
#             break
#         else:
#             print("Invalid option. Please try again.")


# make calls to the initializing and login functions defined above

initializing()
val = login()  # id, role


""" based on the return value for login, activate the code that 
performs activities according to the role defined for that person_id """

# check
memPendReq_table = _database.search('Member_pending_request')
project_table = _database.search('project')
login_table = _database.search('login')

memPendReq_mockdata = [
    {'ProjectID': 'P001', 'to_be_member': '9898118', 'Response': None, 'Response_date': None},
    {'ProjectID': 'P002', 'to_be_member': '9898118', 'Response': None, 'Response_date': None}
]

project_mockdata = [
    {'ProjectID': 'P001', 'Title': 'Project A', 'Lead': None, 'Member1': None, 'Member2': None, 'Advisor': None, 'Status': 'Open'},
    {'ProjectID': 'P002', 'Title': 'Project B', 'Lead': None, 'Member1': None, 'Member2': None, 'Advisor': None, 'Status': 'Open'}
]

# check insert data
for i in range(len(memPendReq_mockdata)):
    memPendReq_table.insert_data(memPendReq_mockdata[i])
# print(memPendReq_table)

# check update data
memPendReq_table.update_data('ProjectID', 'P001', 'Response', 'Accepted')
# print(memPendReq_table)

# check view request
student = Student("9898118", memPendReq_table, project_table)
# print(student.view_requests(memPendReq_table))

# Accept a request and check the changes
# print(student.accept_deny_request("P001", True, memPendReq_table, project_table))
# # Verify if the request has been updated
# print(student.view_requests(memPendReq_table))

# student.handle_requests(memPendReq_table, project_table)

# if val[1] == 'admin':
# see and do admin related activities
if val[1] == 'student':
# see and do student related activities
    student_instance = Student(val[0], memPendReq_table, project_table)

    while True:
            print("\n=== Student Menu ===")
            print("1. View Pending Requests")
            print("2. Accept or Deny Requests")
            print("3. View Project Details")
            print("4. Change Role to Lead")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                student_instance.view_requests(memPendReq_table)
            elif choice == '2':
                student_instance.handle_requests(memPendReq_table, project_table)
            elif choice == '3':
                student_instance.view_requests(memPendReq_table)
                project_id = input("Enter the ProjectID to view details: ")
                student_instance.view_project_details(project_id, project_table)
            elif choice == '4':
                # project_id = input("Enter the ProjectID to change role to lead: ")
                student_instance.change_to_lead(random_project_id, login_table,
                                                memPendReq_table, project_table)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
    # else:
    #     print("Login failed.")

# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everything is done, make a call to the exit function
# exit()


