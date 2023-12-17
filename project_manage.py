# import database module
# import csv, database
from database import *
from datetime import datetime
import random, sys

# define a funcion called initializing

_database = DB()

# Member_pending_request_table = _database.search('Member_pending_request')
# ADVISOR_PENDING_REQUEST = _database.search('Advisor_pending_request')
# PROJECT = _database.search('project')
# LOGIN = _database.search('login')
# PERSON = _database.search('persons')


def generate_random_project_id():
    """
    Generates a random 4-digit ID for a project.
    Returns a string of 4 digits.
    """
    __random_project_id = f"{random.randint(0, 9999):04d}"
    return __random_project_id


random_project_id = generate_random_project_id()


def current_date():
    now = datetime.now()
    formatted_date = now.strftime("%A %B %d, %Y")
    return formatted_date


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
    # project_data = [
    #     {'ProjectID': random_project_id, 'Title': None, 'Lead': None, 'Member1': None,
    #      'Member2': None, 'Advisor': None, 'Status': None}
    # ]
    read_project = ReadCsv('project.csv')
    project_table = Table('project', read_project.data)
    _database.insert(project_table)

    # print(project_table)

    # adPendReq_data = [
    #     {'ProjectID': None, 'to_be_advisor': None, 'Response': None, 'Response_date': None}]
    read_advisorRequest = ReadCsv('Advisor_pending_request.csv')
    advisorRequest_table = Table('Advisor_pending_request',
                                 read_advisorRequest.data)
    _database.insert(advisorRequest_table)

    # print(advisor_pending_request_table)

    # memPendReq_data = [{'ProjectID': None, 'to_be_member': None, 'Response': None, 'Response_date': None}]
    read_memberRequest = ReadCsv('Member_pending_request.csv')
    memberRequest_table = Table('Member_pending_request',
                                read_memberRequest.data)
    _database.insert(memberRequest_table)

    read_examiners_pending = ReadCsv('Examiner_pending_request.csv')
    examiners_pending_table = Table('Examiner_pending_request',
                                    read_examiners_pending.data)
    _database.insert(examiners_pending_table)

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
                    # return None  # Return None if the ID is not found in the persons table
            else:
                print('Password is wrong. Try again.')


# def exit below

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
    _database.write_to_csv()

# function part
############################################################
# class Project:
#     status = {'Pending', 'Approved', 'Completed', 'Cancelled'}
#
#     def __init__(self, projects_csv_path='project.csv'):
#         self.projects_csv_path = projects_csv_path
#         self.projects = self.load_projects_from_csv()
#
#     def load_projects_from_csv(self):
#         projects = []
#         try:
#             with open(self.projects_csv_path, 'r', newline='',
#                       encoding='utf-8') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for row in reader:
#                     projects.append(row)
#         except FileNotFoundError:
#             print(f"File '{self.projects_csv_path}' not found.")
#         except Exception as e:
#             print(
#                 f"Error loading project data from '{self.projects_csv_path}': {e}")
#         return projects
#
#     def get_project(self, project_id):
#         for project in self.projects:
#             if project.get('projectID') == str(project_id):
#                 return project
#         return None
#
#     def modify_project_details(self, project_id, new_title, new_status):
#         for project in self.projects:
#             if project['projectID'] == str(project_id):
#                 project['projectName'] = new_title
#                 project['status'] = new_status
#                 print(f"Project details modified successfully.")
#                 self.save_projects_to_csv()  # Save changes to CSV
#                 return
#
#         print(f"Project with ID {project_id} not found.")
#
#     def save_projects_to_csv(self):
#         try:
#             with open(self.projects_csv_path, 'w', newline='',
#                       encoding='utf-8') as csvfile:
#                 fieldnames = ['projectName', 'projectID', 'leadID',
#                               'advisorName', 'status']
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 writer.writerows(self.projects)
#                 print(
#                     f"Projects saved to '{self.projects_csv_path}' successfully.")
#         except Exception as e:
#             print(f"Error saving projects to '{self.projects_csv_path}': {e}")

def display_all_project():
    proj = _database.search('project').table
    print("All Projects:\n")
    # Header
    print(
        f"{'Project ID':<10} | {'Title':<15} | {'Lead':<10} | {'Member1':<10} | {'Member2':<10} | {'Advisor':<10} | {'Status':<10}")
    print("-" * 90)
    for p in proj:
        print(f"{p.get('ProjectID', 'N/A'):<10} | "
              f"{p.get('Title').strip():<15} | "
              f"{p.get('Lead').strip():<10} | "
              f"{p.get('Member1').strip():<10} | "
              f"{p.get('Member2').strip():<10} | "
              f"{p.get('Advisor').strip():<10} | "
              f"{p.get('Status').strip():<10}")


class Admin:
    def __init__(self, adminID):
        self.adminID = adminID
        # display_all_project()

    @staticmethod
    def get_project_id():
        ask_name = input('Enter Project Name: ')
        PROJECT = _database.search('project')
        for project in PROJECT.table:
            if project['Title'] == ask_name:
                return project[ask_name]
        return None

    @staticmethod
    def get_project_name():
        PROJECT = _database.search('project')
        display_all_project()
        ask_id = input('Enter Project ID: ')
        for project in PROJECT.table:
            if project['ProjectID'] == ask_id:
                return project[ask_id]
        return None

    # @staticmethod
    # def modify_project_info(project_id, new_data):
    #     # Check if the project exists
    #     PROJECT = _database.search('project').table  # Assuming 'project' is the table name
    #     __project_exists = _database.project_id_exists(project_id)
    #     # __project_exists = any(project['ProjectID'] == project_id for project in project_table.table)
    #
    #     if __project_exists:
    #         for key, value in new_data.items():
    #             PROJECT.update_data('ProjectID', project_id, key, value)
    #     else:
    #         PROJECT.insert_data(new_data)

    # def delete_table(self, table_name):
    #     # Code to delete a table from the database
    #     _database.delete(table_name)

    def change_project_status(self):
        while True:
            display_all_project()
            project_id = input("Enter Project ID: ")
            __project_table = _database.search('project').table
            if any(project['ProjectID'] == project_id for project in __project_table):
                break
            else:
                print(f"Project with ID {project_id} not found.")
        # Code to change the status of a project (active/inactive)
        while True:
            new_status = input('Select status to be change((1)ongoing/(2)done): ')
            if new_status == '1':
                new_status = 'ongoing'
                break
            elif new_status == '2':
                new_status = 'done'
                break
            else:
                print('Invalid Input')
        __project_table = _database.search('project')
        __project_table.update_data('ProjectID', project_id, 'Status',
                                    new_status)

    def show_all_professors(self, selected):
        # Code to show all professors
        PERSON = _database.search('persons')
        professors = []
        print('Professor List:')
        for person in PERSON.table:
            if person['type'] == 'faculty' and person not in selected:
                print(f"ID: {person['ID']}, Name: {person['first']} {person['last']}")
                professors.append(person)
        return professors

    # def modify_project_table(self, project_id, new_data):
    #     # Check if the project exists
    #     __project_exists = _database.search('project')  # Assuming 'project' is the table name
    #     # __project_exists = any(project['ProjectID'] == project_id for project in project_table.table)
    #
    #     if __project_exists:
    #         for project in __project_exists.table:
    #             if project['ProjectID'] == project_id:
    #                 for key, value in new_data.items():
    #                     __project_exists.update_data('ProjectID', project_id, key, value)
    #                 break
    #     else:
    #         __project_exists.insert_data(new_data)

    def send_invite(self):
        global project_id
        selected_professor = []
        selected = False

        while not selected:
            table_project = _database.search('project')
            project_id = input("Enter Project ID: ")
            for project in table_project.table:
                if project['ProjectID'] == project_id:
                    selected = True
                    break
                else:
                    print("Invalid Project ID. Please try again.")

        while len(selected_professor) < 3:
            table_professor = self.show_all_professors(selected_professor)
            professor_id = input("Enter Professor ID: ")
            valid = False
            for professor in table_professor:
                if professor['ID'] == professor_id:
                    selected_professor.append(professor)
                    valid = True
                    print(f'Selected: {len(selected_professor)} examiners.')
                    break
            if not valid:
                print("Invalid Professor ID. Please try again.")

        for professor in selected_professor:
            examiner_pending = _database.search('Examiner_pending_request')
            examiner_pending.insert_data(
                {'ProjectID': project_id, 'to_be_examiners': professor['ID'],
                 'response': 'None', 'response_date': 'None'})
        return

    def delete_project(self):
        while True:
            display_all_project()
            project_id = input("Enter Project ID: ")
            __project_table = _database.search('project').table
            index_to_remove = next((index for index, entry in enumerate(__project_table) if
                                    entry.get('ProjectID') == project_id), None)
            if index_to_remove is not None:
                __project_table.pop(index_to_remove)
                break
            else:
                print(f"Project with ID {project_id} not found.")

class Student:
    def __init__(self, sIDfromlogin):
        self.ID = self.get_id_from_username(sIDfromlogin)
        # self.IN_GROUP = False

    @staticmethod
    def get_id_from_username(sIDfromlogin):
        return sIDfromlogin

    # def get_member_status(self, table):
    #     for request in table.table:
    #         if request['to_be_member'] == self.ID:
    #             return request['Response']
    #     return None
    # def get_member_status(self, member_request_data):
    #     for request in member_request_data.table:
    #         # Adjust the keys to match the data structure
    #         if request.get('to_be_member') == self.ID:
    #             return request.get('Response')
    #     return None

    def get_project_id(self):
        display_all_project()

    def view_requests(self):
        # Filter requests where 'to_be_member' matches 'self.ID'
        print(
            f"{'Project ID':<10} | {'To Be Member':<15} | {'Response':<10} | {'Response Date':<15}")
        print("-" * 60)  # Print a separator line
        Member_pending_request = _database.search(
            'Member_pending_request').table
        avalable_project = []
        # Iterate over the data and print relevant requests
        for request in Member_pending_request:
            to_be_member = request.get('to_be_member',
                                       'N/A')
            response = request.get('Response').strip()
            if to_be_member == self.ID and response == 'None':
                # print(self.print_request(self.ID))
                project_id = request.get('ProjectID').strip()
                to_be_member = request.get('to_be_member').strip()
                response = request.get('Response').strip()
                response_date = request.get('Response_date').strip()
                print(
                    f"{project_id:<10} | {to_be_member:<15} | {response:<10} | {response_date:<15}")
                avalable_project.append(project_id)
        return avalable_project

    def get_request(self):
        Member_pending_request = _database.search(
            'Member_pending_request').table
        matching_requests = []

        for request in Member_pending_request:
            to_be_member = request.get('to_be_member', 'N/A').strip()
            if to_be_member == self.ID:
                uniqueID = request.get('uniqueID', 'N/A').strip()
                project_id = request.get('ProjectID', 'N/A').strip()
                response = request.get('Response', 'N/A').strip()
                response_date = request.get('Response_date', 'N/A').strip()
                matching_requests.append({
                    'uniqueID': uniqueID,
                    'ProjectID': project_id,
                    'To Be Member': to_be_member,
                    'Response': response,
                    'Response Date': response_date
                })

        return matching_requests

    def update_project_member(self, Project_ID):
        PROJECT = _database.search('project')
        for project in PROJECT.table:
            P_ID = project.get('ProjectID', 'N/A')
            if P_ID == Project_ID:
                slot1 = project.get('Member1')
                slot2 = project.get('Member2')
                print(slot1, slot2)
                if slot1 == "None":
                    PROJECT.update_data('ProjectID', Project_ID,
                                                 'Member1', self.ID)
                    self.IN_GROUP = True
                elif slot2 == "None":
                    PROJECT.update_data('ProjectID', Project_ID,
                                                 'Member2', self.ID)
                    self.IN_GROUP = True
                else:
                    print('Project Team already full')

    def accept_deny_request(self, getprojectID, decision):
        MEMBER_PENDING_REQUEST = _database.search('Member_pending_request')
        all_project_request = self.get_request()
        for eachProject in all_project_request:
            if eachProject['ProjectID'] == getprojectID:
                if decision.lower() == 'accept':
                    MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                             eachProject[
                                                                 'uniqueID'],
                                                             'Response',
                                                             'Accept')
                    MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                             eachProject[
                                                                 'uniqueID'],
                                                             'Response_date',
                                                             current_date())
                    self.update_project_member(eachProject['ProjectID'])
                elif decision.lower() == 'deny':
                    MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                       eachProject['uniqueID'],
                                                       'Response', 'Deny')
                    MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                       eachProject['uniqueID'],
                                                       'Response_date',
                                                       current_date())

    def handle_requests(self):
        print('Project Invitation:')
        requests = self.view_requests()

        while True:
            request_id = input(
                "Enter the ProjectID to respond to (or 'exit' to cancel): ")
            if request_id in requests:
                break
            if request_id.lower() == 'exit':
                return

        response = input("Do you want to accept (type 'accept') or deny (type 'deny') the request?: ")
        if response.lower() in ['accept', 'deny']:
            self.accept_deny_request(request_id, response)
            print("Request response updated.")
        else:
            print("Invalid response. No action taken.")

    def change_to_lead(self):
        """
        Change the role to 'lead' for a project. Update project_table and login table.
        Must deny all member requests before changing the role.
        """
        # Implementation details will vary based on how roles and requests are handled

        MEMBER_PENDING_REQUEST = _database.search('Member_pending_request').table
        PROJECT = _database.search('project').table
        LOGIN = _database.search('login').table

        projectID = f'P{len(PROJECT)+1}'

        # Deny all pending member requests for the specified project
        for request in MEMBER_PENDING_REQUEST:
            if request['to_be_member'] == self.ID:
                request['Response'] = 'Denied'

        # Check if this student is already a lead in any project
        is_already_lead = any(project['Lead'] == self.ID for project in PROJECT)

        if is_already_lead:
            print("This student is already a project lead.")
        else:
            # If not a lead, create or update a project
            # is_already_lead = False
            for project in PROJECT:
                if project['ProjectID'] == projectID:
                    project['Lead'] = self.ID
                    is_already_lead = True
                    break

            if not is_already_lead:
                ask_newProjectName = input('Enter new project name: ')
                new_project = {'ProjectID': projectID, 'Title': ask_newProjectName,
                               'Lead': self.ID, 'Member1': 'None',
                               'Member2': 'None', 'Advisor': 'None',
                               'Status': 'ongoing'}
                PROJECT.append(new_project)
                print(f"Role changed to 'lead' for project {projectID}. New project created.")

# class Lead:

# main part

# make calls to the initializing and login functions defined above


initializing()
val = login()  # id, role

""" based on the return value for login, activate the code that 
performs activities according to the role defined for that person_id """

# check
# Member_pending_request_table = _database.search('Member_pending_request')
# Advisor_pending_request_table = _database.search('Advisor_pending_request')
# project_table = _database.search('project')
# login_table = _database.search('login')
# personTable = _database.search('persons')

# memPendReq_mockdata = [
#     {'ProjectID': 'P001', 'to_be_member': '9898118', 'Response': None, 'Response_date': None},
#     {'ProjectID': 'P002', 'to_be_member': '9898118', 'Response': None, 'Response_date': None}
# ]

# project_mockdata = [
#     {'ProjectID': 'P001', 'Title': 'Project A', 'Lead': None, 'Member1': None, 'Member2': None, 'Advisor': None, 'Status': 'Open'},
#     {'ProjectID': 'P002', 'Title': 'Project B', 'Lead': None, 'Member1': None, 'Member2': None, 'Advisor': None, 'Status': 'Open'}
# ]

# check insert data
# for i in range(len(memPendReq_mockdata)):
#     memPendReq_table.insert_data(memPendReq_mockdata[i])
# print(memPendReq_table)

# check update data
# memPendReq_table.update_data('ProjectID', 'P001', 'Response', 'Accepted')
# print(memPendReq_table)

# check view request
# student = Student("9898118", memPendReq_table, project_table)
# print(student.view_requests(memPendReq_table))


# Accept a request and check the changes
# print(student.accept_deny_request("P001", True, memPendReq_table, project_table))
# # Verify if the request has been updated
# print(student.view_requests(memPendReq_table))

# student.handle_requests(memPendReq_table, project_table)
# print(use_memberReq_table)  # Print first 5 elements for inspection

if val[1] == 'admin':
    # see and do admin related activities
    admin_instance = Admin(val[0])

    while True:
        print("\n=== Admin Menu ===")
        # print("1. Modify Project Info")
        print("1. Send Invite to Examinors")
        print("2. Change Project Status")
        print("3. Delete Project")
        print("4. Exit (to save changes)")

        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            # project_id = input("Enter Project ID: ")
            display_all_project()
            admin_instance.send_invite()
            # new_data = {}  # Collect new data for project
            # # Populate new_data dictionary with user input
            # # Example: new_data['Title'] = input("Enter new title: ")
            # admin_instance.modify_project_info(project_id, new_data)
        elif choice == '2':
            admin_instance.change_project_status()
        elif choice == '3':
            admin_instance.delete_project()
        elif choice == '4':
            exit()
            break
            # project_id = input("Enter Project ID: ")
            # admin_instance.change_project_status(project_id)
        # elif choice == '4':
        #     exit()
        else:
            print("Invalid choice. Please try again.")


elif val[1] == 'student':
    # see and do student related activities
    # student_instance = Student(val[0], use_memberReq_table, use_project_table)
    student_instance = Student(val[0])
    # student_instance = Student(val[0], Member_pending_request_table,
    #                            project_table)
    # student_instance = Student(login_table, Member_pending_request_table, project_table)

    # student_instance.handle_requests()

    while True:
        print("\n=== Student Menu ===")
        print("1. View Pending Requests")
        print("2. Accept or Deny Requests")
        # print("3. View Project Details")
        print("3. Change Role to Lead")
        print("4. Exit (to save changes)")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_instance.view_requests()
        elif choice == '2':
            student_instance.handle_requests()
        elif choice == '3':
            student_instance.change_to_lead()
        elif choice == '4':
            exit()
            break
        else:
            print("Invalid choice. Please try again.")
#
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
