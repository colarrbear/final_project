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

    read_login = ReadCsv('login.csv')
    login_table = Table('login', read_login.data)
    _database.insert(login_table)

    read_project = ReadCsv('project.csv')
    project_table = Table('project', read_project.data)
    _database.insert(project_table)

    read_advisorRequest = ReadCsv('Advisor_pending_request.csv')
    advisorRequest_table = Table('Advisor_pending_request',
                                 read_advisorRequest.data)
    _database.insert(advisorRequest_table)


    read_memberRequest = ReadCsv('Member_pending_request.csv')
    memberRequest_table = Table('Member_pending_request',
                                read_memberRequest.data)
    _database.insert(memberRequest_table)

    read_examiners_pending = ReadCsv('Examiner_pending_request.csv')
    examiners_pending_table = Table('Examiner_pending_request',
                                    read_examiners_pending.data)
    _database.insert(examiners_pending_table)

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
        login_table = _database.search('login')

        user_found = None
        for user in login_table.table:
            if user['username'] == username:
                user_found = user
                break

        if user_found:
            password = input("Enter password: ")
            if user_found['password'] == password:
                login_table = _database.search('login')
                for person in login_table.table:
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

    def get_project_id(self):
        display_all_project()

    def view_requests(self):
        Member_pending_request = _database.search(
            'Member_pending_request').table
        available_projects = []

        # Filter requests where 'to_be_member' matches 'self.ID' and the response is 'None'
        for request in Member_pending_request:
            to_be_member = request.get('to_be_member', 'N/A').strip()
            response = request.get('Response', 'N/A').strip()
            if to_be_member == self.ID and response == 'None':
                project_id = request.get('ProjectID', 'N/A').strip()
                response_date = request.get('Response_date', 'N/A').strip()
                available_projects.append({
                    'ProjectID': project_id,
                    'To Be Member': to_be_member,
                    'Response': response,
                    'Response Date': response_date
                })

        # Check if there are any available requests
        if available_projects:
            print("\nPending Requests:")
            print(
                f"{'Project ID':<10} | {'To Be Member':<15} | {'Response':<10} | {'Response Date':<15}")
            print("-" * 60)  # Print a separator line
            for project in available_projects:
                print(
                    f"{project['ProjectID']:<10} | {project['To Be Member']:<15} | {project['Response']:<10} | {project['Response Date']:<15}")
        else:
            print("\nNo requests found.")

        return [project['ProjectID'] for project in available_projects]
        # Filter requests where 'to_be_member' matches 'self.ID'
        # print()
        # print(f"{'Project ID':<10} | {'To Be Member':<15} | {'Response':<10} | {'Response Date':<15}")
        # print("-" * 60)  # Print a separator line
        # Member_pending_request = _database.search(
        #     'Member_pending_request').table
        # avalable_project = []
        # # Iterate over the data and print relevant requests
        # for request in Member_pending_request:
        #     to_be_member = request.get('to_be_member',
        #                                'N/A')
        #     response = request.get('Response').strip()
        #     if to_be_member == self.ID and response == 'None':
        #         # print(self.print_request(self.ID))
        #         project_id = request.get('ProjectID').strip()
        #         to_be_member = request.get('to_be_member').strip()
        #         response = request.get('Response').strip()
        #         response_date = request.get('Response_date').strip()
        #         print(
        #             f"{project_id:<10} | {to_be_member:<15} | {response:<10} | {response_date:<15}")
        #         avalable_project.append(project_id)
        # return avalable_project

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
                # print(slot1, slot2)
                if slot1 == 'None':
                    PROJECT.update_data('ProjectID',Project_ID,'Member1', self.ID)
                    return True  # Member added successfully
                    # self.IN_GROUP = True
                elif slot2 == "None":
                    PROJECT.update_data('ProjectID', Project_ID,'Member2', self.ID)
                    return True  # Member added successfully
                    # self.IN_GROUP = True
                else:
                    print('Project Team already full')
                    return False  # Project is full
        return False  # Project not found or other error

    def is_already_in_project(self):
        PROJECT = _database.search('project')
        for project in PROJECT.table:
            if project.get('Member1') == self.ID or project.get('Member2') == self.ID:
                return True
        return False

    def accept_deny_request(self, getprojectID, decision):
        MEMBER_PENDING_REQUEST = _database.search('Member_pending_request')
        all_project_request = self.get_request()
        for eachProject in all_project_request:
            if eachProject['ProjectID'] == getprojectID:
                if decision.lower() == 'accept':
                    # Check if the student is already in a project
                    if self.is_already_in_project():
                        print("You are already in a project.")
                        return  # Exit the function
                    # Update the selected project request and add the student to the project
                    updated = self.update_project_member(
                        eachProject['ProjectID'])
                    if updated:
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
                        # Automatically deny all other pending requests
                        for otherProject in all_project_request:
                            if otherProject['ProjectID'] != getprojectID:
                                MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                                   otherProject[
                                                                       'uniqueID'],
                                                                   'Response',
                                                                   'Deny')
                                MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                                   otherProject[
                                                                       'uniqueID'],
                                                                   'Response_date',
                                                                   current_date())
                elif decision.lower() == 'deny':
                    # Only deny the selected project request
                    MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                       eachProject['uniqueID'],
                                                       'Response', 'Deny')
                    MEMBER_PENDING_REQUEST.update_data('uniqueID',
                                                       eachProject['uniqueID'],
                                                       'Response_date',
                                                       current_date())

    # def accept_deny_request(self, getprojectID, decision):
    #     MEMBER_PENDING_REQUEST = _database.search('Member_pending_request')
    #     all_project_request = self.get_request()
    #     for eachProject in all_project_request:
    #         if eachProject['ProjectID'] == getprojectID:
    #             if decision.lower() == 'accept':
    #                 # Update the selected project request
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                    eachProject['uniqueID'],
    #                                                    'Response',
    #                                                    'Accept')
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                    eachProject['uniqueID'],
    #                                                    'Response_date',
    #                                                    current_date())
    #                 self.update_project_member(eachProject['ProjectID'])
    #
    #                 # Automatically deny all other pending requests
    #                 for otherProject in all_project_request:
    #                     if otherProject['ProjectID'] != getprojectID:
    #                         MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                            otherProject[
    #                                                                'uniqueID'],
    #                                                            'Response',
    #                                                            'Deny')
    #                         MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                            otherProject[
    #                                                                'uniqueID'],
    #                                                            'Response_date',
    #                                                            current_date())
    #             elif decision.lower() == 'deny':
    #                 # Only deny the selected project request
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                    eachProject['uniqueID'],
    #                                                    'Response', 'Deny')
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                    eachProject['uniqueID'],
    #                                                    'Response_date',
    #                                                    current_date())

    # def accept_deny_request(self, getprojectID, decision):
    #     MEMBER_PENDING_REQUEST = _database.search('Member_pending_request')
    #     all_project_request = self.get_request()
    #     for eachProject in all_project_request:
    #         if eachProject['ProjectID'] == getprojectID:
    #             if decision.lower() == 'accept':
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                          eachProject[
    #                                                              'uniqueID'],
    #                                                          'Response',
    #                                                          'Accept')
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                          eachProject[
    #                                                              'uniqueID'],
    #                                                          'Response_date',
    #                                                          current_date())
    #                 self.update_project_member(eachProject['ProjectID'])
    #             elif decision.lower() == 'deny':
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                    eachProject['uniqueID'],
    #                                                    'Response', 'Deny')
    #                 MEMBER_PENDING_REQUEST.update_data('uniqueID',
    #                                                    eachProject['uniqueID'],
    #                                                    'Response_date',
    #                                                    current_date())

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

    def is_already_lead(self):
        PROJECT = _database.search('project').table
        return any(project['Lead'] == self.ID for project in PROJECT)

class Lead:
    def __init__(self, student):
        # self.student.ID
        if not isinstance(student, Student):
            raise ValueError("Invalid student instance")
        self.student = student
        self.myProject = self.get_project()

    def get_project(self):
        # display_all_project()
        PROJECT = _database.search('project')
        for project in PROJECT.table:
            if self.student.ID == project.get("Lead"):
                return project

    def perform_lead_duties(self):
        if self.student.is_already_lead():
            # Perform lead-specific functionalities
            print(f"Student ID {self.student.ID} is a lead for a project.")
            # Additional lead duties can be implemented here
        else:
            print("This student is not a lead. Please assign lead responsibilities first.")

    def see_project_status(self):
        PROJECT = _database.search('project').table
        MEMBER_PENDING_REQUEST = _database.search(
            'Member_pending_request').table
        ADVISOR_PENDING_REQUEST = _database.search(
            'Advisor_pending_request').table

        project_id = self.myProject['ProjectID']
        current_project = next(
            (proj for proj in PROJECT if proj['ProjectID'] == project_id),
            None)

        # Check if both member slots are filled and an advisor is assigned
        if current_project and current_project['Member1'] not in [None, 'None',
                                                                  ''] and \
                current_project['Member2'] not in [None, 'None', ''] and \
                current_project['Advisor'] not in [None, 'None', '']:
            status = "Ongoing"

        else:
            # Check pending status based on member and advisor requests
            members_pending = any(
                req['ProjectID'] == project_id and req['Response'] == 'None'
                for req in MEMBER_PENDING_REQUEST)
            advisor_pending = any(
                req['ProjectID'] == project_id and req['Response'] == 'None'
                for req in ADVISOR_PENDING_REQUEST)

            if members_pending:
                status = "Pending Member"
            elif advisor_pending:
                status = "Pending Advisor"
            else:
                status = "Ready to Solicit an Advisor"
        print(f"Project Status: {status}")

    def modify_project_info(self):
        # project_id = self.myProject['ProjectID']
        project_info = self.myProject  # project
        print("\nCurrent Project Info:")

        headers = ["Attribute", "Value"]
        print(f"{headers[0]:<15} | {headers[1]:<15}")
        print("-" * 32)  # Separator line for header
        for key, value in project_info.items():
            print(f"{key:<15} | {str(value):<15}")

        new_title = input(
            "\nEnter new title (leave blank to keep current): ")
        # if leave it blank, need to click enter twice
        new_status = input(
            "\nEnter new status (leave blank to keep current): ")


        # Update if necessary
        if new_title:
            project_info['Title'] = new_title
            print('Project title successfully updated')

        if new_status:
            project_info['Status'] = new_status
            print('Project status successfully updated')

    def view_responses_to_requests(self):
        PROJECT = _database.search('project').table
        MEMBER_PENDING_REQUEST = _database.search(
            'Member_pending_request').table
        ADVISOR_PENDING_REQUEST = _database.search(
            'Advisor_pending_request').table
        project_id = self.myProject['ProjectID']

        # Check current project details
        current_project = next(
            (proj for proj in PROJECT if proj['ProjectID'] == project_id),
            None)

        # Check if project already has 2 members
        if current_project and current_project['Member1'] not in [None, 'None',
                                                                  ''] and \
                current_project['Member2'] not in [None, 'None', '']:
            print(
                f"Your project (ID: {project_id}) already has 2 members. No pending member requests.")
        else:
            # Print member responses in a table format
            print("\nMember Responses:")
            print(
                f"{'Unique ID':<10} | {'Project ID':<10} | {'Member ID':<10} | {'Response':<10} | {'Response Date':<15}")
            print("-" * 60)
            for resp in MEMBER_PENDING_REQUEST:
                if resp['ProjectID'] == project_id:
                    print(
                        f"{resp.get('uniqueID', 'N/A'):<10} | {resp.get('ProjectID', 'N/A'):<10} | {resp.get('to_be_member', 'N/A'):<10} | {resp.get('Response', 'N/A'):<10} | {resp.get('Response_date', 'N/A'):<15}")

        # Check if project already has an advisor
        if current_project and current_project['Advisor'] not in [None, 'None',
                                                                  '']:
            print(
                f"Your project (ID: {project_id}) already has an advisor. No pending advisor requests.")
        else:
            # Print advisor responses in a table format
            print("\nAdvisor Responses:")
            print(
                f"{'Project ID':<10} | {'Advisor ID':<10} | {'Response':<10} | {'Response Date':<15}")
            print("-" * 60)
            for resp in ADVISOR_PENDING_REQUEST:
                if resp['ProjectID'] == project_id:
                    print(
                        f"{resp.get('ProjectID', 'N/A'):<10} | {resp.get('to_be_advisor', 'N/A'):<10} | {resp.get('Response', 'N/A'):<10} | {resp.get('Response_date', 'N/A'):<15}")

    # def view_responses_to_requests(self):
    #     MEMBER_PENDING_REQUEST = _database.search('Member_pending_request').table
    #     ADVISOR_PENDING_REQUEST = _database.search('Advisor_pending_request').table
    #     project_id = self.myProject['ProjectID']
    #
    #     member_responses = [req for req in MEMBER_PENDING_REQUEST if req['ProjectID'] == project_id]
    #     advisor_responses = [req for req in ADVISOR_PENDING_REQUEST if req['ProjectID'] == project_id]

    #     print("\nMember Responses:")
    #     print(
    #         f"{'Unique ID':<10} | {'Project ID':<10} | {'Member ID':<10} | {'Response':<10} | {'Response Date':<15}")
    #     print("-" * 60)
    #     for resp in member_responses:
    #         print(
    #             f"{resp.get('uniqueID', 'N/A'):<10} | {resp.get('ProjectID', 'N/A'):<10} | {resp.get('to_be_member', 'N/A'):<10} | {resp.get('Response', 'N/A'):<10} | {resp.get('Response_date', 'N/A'):<15}")
    #
    #     # Print advisor responses in a table format
    #     print("\nAdvisor Responses:")
    #     print(
    #         f"{'Project ID':<10} | {'Advisor ID':<10} | {'Response':<10} | {'Response Date':<15}")
    #     print("-" * 60)
    #     for resp in advisor_responses:
    #         print(f"{resp.get('ProjectID', 'N/A'):<10} | {resp.get('to_be_advisor', 'N/A'):<10} | {resp.get('Response', 'N/A'):<10} | {resp.get('Response_date', 'N/A'):<15}")

    # def send_request_to_member(self, member_id):
    #     MEMBER_PENDING_REQUEST = _database.search('Member_pending_request').table
    #     project_id = self.myProject['ProjectID']
    #
    #     uniqueID = len(MEMBER_PENDING_REQUEST)+1
    #     # Add request to the table
    #     new_request = {'uniqueID': uniqueID,'ProjectID': project_id, 'to_be_member': member_id, 'Response': 'None', 'Response_date': 'None'}
    #     MEMBER_PENDING_REQUEST.append(new_request)
    #     print('Request for Project Membership sent.')
    def send_request_to_member(self):
        PROJECT = _database.search('project').table
        MEMBER_PENDING_REQUEST = _database.search('Member_pending_request').table
        project_id = self.myProject['ProjectID']

        # Retrieve the current project information
        current_project = next((proj for proj in PROJECT if proj['ProjectID'] == project_id), None)

        # Check if both member slots are filled
        if current_project and current_project['Member1'] not in [None, 'None', ''] and current_project['Member2'] not in [None, 'None', '']:
            print(f'Your project (ID: {project_id}) already has 2 members. Cannot send more invites.')
            return

        # Ask for the member ID to send the request
        ask_member_id = input("\nEnter Member ID to send request: ")
        if ask_member_id.strip() == '':
            return

        # Generate a unique ID for the new request
        uniqueID = len(MEMBER_PENDING_REQUEST) + 1

        # Add request to the table
        new_request = {'uniqueID': uniqueID, 'ProjectID': project_id, 'to_be_member': ask_member_id, 'Response': 'None', 'Response_date': 'None'}
        MEMBER_PENDING_REQUEST.append(new_request)
        print('Request for Project Membership sent.')

    def send_request_to_advisor(self):
        PROJECT = _database.search('project').table
        ADVISOR_PENDING_REQUEST = _database.search('Advisor_pending_request').table
        project_id = self.myProject['ProjectID']

        # Retrieve the current project information
        current_project = next((proj for proj in PROJECT if proj['ProjectID'] == project_id), None)

        # Check if an advisor already exists
        if current_project and current_project['Advisor'] not in [None, 'None', '']:
            print(f'Your project (ID: {project_id}) already has an advisor. Cannot send more invites.')
            return

        # Check if both member slots are filled
        if not (current_project['Member1'] not in [None, 'None', ''] and current_project['Member2'] not in [None, 'None', '']):
            print(f'Cannot invite advisor until both member slots are filled for the project (ID: {project_id}).')
            return

        # Ask for the advisor ID to send the request
        ask_advisor_id = input("\nEnter Advisor ID to send request: ")

        # Add request to the table
        new_request = {'ProjectID': project_id, 'to_be_advisor': ask_advisor_id, 'Response': 'None', 'Response_date': 'None'}
        ADVISOR_PENDING_REQUEST.append(new_request)
        print('Request for Advisor sent.')


class Member:
    def __init__(self, student):
        if not isinstance(student, Student):
            raise ValueError("Invalid student instance")
        self.student = student
        self.myProject = self.get_project()

    def get_project(self):
        PROJECT = _database.search('project')
        for project in PROJECT.table:
            if self.student.ID == project.get("Member1") or self.student.ID == project.get("Member2"):
                return project

    def is_already_member(self):
        return bool(self.myProject)

    def see_project_status(self):
        MEMBER_PENDING_REQUEST = _database.search('Member_pending_request').table
        ADVISOR_PENDING_REQUEST = _database.search('Advisor_pending_request').table

        # Assuming the student's project ID is stored in self.student.projectID
        project_id = self.myProject['ProjectID']
        current_project = next(
            (proj for proj in PROJECT if proj['ProjectID'] == project_id),
            None)

        # Check if both member slots are filled and an advisor is assigned
        if current_project and current_project['Member1'] not in [None, 'None',
                                                                  ''] and \
                current_project['Member2'] not in [None, 'None', ''] and \
                current_project['Advisor'] not in [None, 'None', '']:
            status = "Ongoing"

        else:
            members_pending = any(
                req['ProjectID'] == project_id and req['Response'] == 'None' for
                req in MEMBER_PENDING_REQUEST)
            advisor_pending = any(
                req['ProjectID'] == project_id and req['Response'] == 'None' for
                req in ADVISOR_PENDING_REQUEST)

            if members_pending:
                status = "Pending Member"
            elif advisor_pending:  # advisor_pending
                status = "Pending Advisor"
            else:
                status = "Waiting for lead to invite an advisor"

        print(f"Project Status: {status}")

    def modify_project_info(self):
        project_info = self.myProject  # project
        print("\nCurrent Project Info:")

        headers = ["Attribute", "Value"]
        print(f"{headers[0]:<15} | {headers[1]:<15}")
        print("-" * 32)
        for key, value in project_info.items():
            print(f"{key:<15} | {str(value):<15}")

        new_title = input(
            "\nEnter new title (leave blank to keep current): ")
        # if leave it blank, need to click enter twice
        new_status = input(
            "\nEnter new status (leave blank to keep current): ")


        # Update if necessary
        if new_title:
            project_info['Title'] = new_title
            print('Project title successfully updated')

        if new_status:
            project_info['Status'] = new_status
            print('Project status successfully updated')


    def view_responses_to_requests(self):
        MEMBER_PENDING_REQUEST = _database.search('Member_pending_request').table
        ADVISOR_PENDING_REQUEST = _database.search('Advisor_pending_request').table
        project_id = self.myProject['ProjectID']

        member_responses = [req for req in MEMBER_PENDING_REQUEST if req['ProjectID'] == project_id]
        advisor_responses = [req for req in ADVISOR_PENDING_REQUEST if req['ProjectID'] == project_id]

        print("\nMember Responses:")
        print(
            f"{'Unique ID':<10} | {'Project ID':<10} | {'Member ID':<10} | {'Response':<10} | {'Response Date':<15}")
        print("-" * 60)
        for resp in member_responses:
            print(
                f"{resp.get('uniqueID', 'N/A'):<10} | {resp.get('ProjectID', 'N/A'):<10} | {resp.get('to_be_member', 'N/A'):<10} | {resp.get('Response', 'N/A'):<10} | {resp.get('Response_date', 'N/A'):<15}")

        # Print advisor responses in a table format
        print("\nAdvisor Responses:")
        print(
            f"{'Project ID':<10} | {'Advisor ID':<10} | {'Response':<10} | {'Response Date':<15}")
        print("-" * 60)
        for resp in advisor_responses:
            print(f"{resp.get('ProjectID', 'N/A'):<10} | {resp.get('to_be_advisor', 'N/A'):<10} | {resp.get('Response', 'N/A'):<10} | {resp.get('Response_date', 'N/A'):<15}")


class Faculty:
    def __init__(self, sIDfromlogin):
        self.ID = self.get_id_from_username(sIDfromlogin)

    @staticmethod
    def get_id_from_username(sIDfromlogin):
        return sIDfromlogin

    def view_advisor_requests(self):
        ADVISOR_PENDING_REQUEST = _database.search(
            'Advisor_pending_request').table
        requests = [req for req in ADVISOR_PENDING_REQUEST if
                    req['to_be_advisor'] == self.ID]
        print("Advisor Requests:")
        for req in requests:
            print(f"Project ID: {req['ProjectID']}, Response: {req['Response']}, Date: {req['Response_date']}")

    def send_advisor_response(self):
        ADVISOR_PENDING_REQUEST = _database.search(
            'Advisor_pending_request').table
        self.view_advisor_requests()
        project_id = input("Enter the Project ID for which to send response: ")
        response = input("Enter your response (Accept/Deny): ")

        valid_request = next((req for req in ADVISOR_PENDING_REQUEST if
                              req['ProjectID'] == project_id and req[
                                  'to_be_advisor'] == self.ID), None)
        if valid_request:
            valid_request['Response'] = response
            valid_request['Response_date'] = current_date()
            print("Response sent successfully.")
        else:
            print("No matching request found.")

    def view_examiner_requests(self):
        EXAMINER_PENDING_REQUEST = _database.search('Examiner_pending_request').table
        requests = [req for req in EXAMINER_PENDING_REQUEST if req['to_be_examiners'] == self.ID]
        print("Examiner Requests:")
        for req in requests:
            print(f"Project ID: {req['ProjectID']}, Response: {req['Response']}, Date: {req['Response_date']}")

    def send_examiners_response(self):
        EXAMINER_PENDING_REQUEST = _database.search('Examiner_pending_request').table
        self.view_examiner_requests()
        project_id = input("Enter the Project ID for which to send response: ")
        response = input("Enter your response (Accept/Deny): ")

        valid_request = next((req for req in EXAMINER_PENDING_REQUEST if req['ProjectID'] == project_id and req['to_be_examiners'] == self.ID), None)
        if valid_request:
            valid_request['Response'] = response
            valid_request['Response_date'] = current_date()
            print("Response sent successfully.")
        else:
            print("No matching request found.")


class Advisor(Faculty):
    def __init__(self, sIDfromlogin):
        super().__init__(sIDfromlogin)

    def modify_project(self):
        PROJECT = _database.search('project').table
        project_id = input("Enter the Project ID to modify: ")

        # Fetch and display current project information
        project_info = next((p for p in PROJECT if p['ProjectID'] == project_id), None)
        if project_info:
            print("Current Project Info:")

            headers = ["Attribute", "Value"]
            print(f"{headers[0]:<15} | {headers[1]:<15}")
            print("-" * 32)  # Separator line for header
            for key, value in project_info.items():
                print(f"{key:<15} | {str(value):<15}")

            # Ask for new details
            new_title = input("Enter new title (leave blank to keep current): ")
            new_status = input("Enter new status (leave blank to keep current): ")

            # Update if necessary
            if new_title:
                project_info['Title'] = new_title
            if new_status:
                project_info['Status'] = new_status

            # Update the database
            PROJECT.update_data('ProjectID', project_id, 'Title', new_title)
            PROJECT.update_data('ProjectID', project_id, 'Status', new_status)
            print("Project updated successfully.")
        else:
            print("Project not found.")

    def approve_project(self):
        PROJECT = _database.search('project').table
        project_id = input("Enter the Project ID to approve: ")

        project_info = next((p for p in PROJECT if p['ProjectID'] == project_id), None)
        if project_info:
            project_info['Status'] = 'Approved'
            PROJECT.update_data('ProjectID', project_id, 'Status', 'Approved')
            print(f"Project {project_id} approved successfully.")
        else:
            print("Project not found.")


# ... [main function] ...
# Member class can now be used similarly to Student and Lead classes in the main part of the program.
# make calls to the initializing and login functions defined above


initializing()
val = login()  # id, role

""" based on the return value for login, activate the code that 
performs activities according to the role defined for that person_id """


if val[1] == 'student':
    student_instance = Student(val[0])
    # Check role in project (Lead, Member, or neither)
    PROJECT = _database.search('project').table
    is_lead = any(project['Lead'] == val[0] for project in PROJECT)
    is_member = any(
        project['Member1'] == val[0] or project['Member2'] == val[0] for
        project in PROJECT)

    if is_lead:  # need to fix function
        # Lead functionalities
        lead_instance = Lead(student_instance)
        while True:
            print("\n=== Lead Menu ===")
            print("1. View Project Status")
            print("2. Modify/View Project Info")
            print("3. View Responses to Requests")
            print("4. Send Request to Member")
            print("5. Send Request to Advisor")
            print("6. Exit")
            choice = input("\nEnter your choice: ")
            if choice == '1':
                lead_instance.see_project_status()
            elif choice == '2':
                lead_instance.modify_project_info()
            elif choice == '3':
                lead_instance.view_responses_to_requests()
            elif choice == '4':
                lead_instance.send_request_to_member()
            elif choice == '5':
                lead_instance.send_request_to_advisor()
            elif choice == '6':
                break

    elif is_member:
        # Member functionalities
        member_instance = Member(student_instance)
        while True:
            print("\n=== Member Menu ===")
            print("1. View Project Status")
            print("2. Modify/View Project Info")
            print("3. View Responses to Requests")
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                member_instance.see_project_status()
            elif choice == '2':
                member_instance.modify_project_info()
            elif choice == '3':
                member_instance.view_responses_to_requests()
            elif choice == '4':
                break

    else:
        # General student functionalities
        while True:  # finish
            print("\n=== Student Menu ===")
            print("1. View Pending Requests")
            print("2. Accept or Deny Requests")
            print("3. Create project")  # Change Role to Lead
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                student_instance.view_requests()
            elif choice == '2':
                student_instance.handle_requests()
            elif choice == '3':
                student_instance.change_to_lead()
            elif choice == '4':
                break

# doesn't update code below

elif val[1] == 'admin':
    # see and do admin related activities
    admin_instance = Admin(val[0])

    while True:
        print("\n=== Admin Menu ===")
        print("1. Send Invite to Examinors")
        print("2. Change Project Status")
        print("3. Delete Project")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        print()
        if choice == '1':
            display_all_project()
            admin_instance.send_invite()
        elif choice == '2':
            admin_instance.change_project_status()
        elif choice == '3':
            admin_instance.delete_project()
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")

elif val[1] == 'faculty':
    faculty_instance = Faculty(val[0])
    while True:
        print("\n=== Faculty Menu ===")
        print("1. View Advisor Requests")
        print("2. Respond to Advisor Request")
        print("3. View Examiner Requests")
        print("4. Respond to Examiner Request")
        print("5. Exit")
        print()
        choice = input("\nEnter your choice: ")
        print()
        if choice == '1':
            faculty_instance.view_advisor_requests()
        elif choice == '2':
            faculty_instance.send_advisor_response()
        elif choice == '3':
            faculty_instance.view_examiner_requests()
        elif choice == '4':
            faculty_instance.send_examiners_response()
        elif choice == '5':
            break
        else:
            print("\nInvalid choice. Please try again.")

elif val[1] == 'advisor':
    faculty_instance = Faculty(val[0])
    advisor_instance = Advisor(faculty_instance)
    while True:
        print("\n=== Advisor Menu ===")
        print("1. View Advisor Requests")
        print("2. Send Advisor Response")
        print("3. View Examiner Requests")
        print("4. Send Examiner Response")
        print("5. Modify Project")
        print("6. Approve Project")
        print("7. Exit")
        print()
        choice = input("\nEnter your choice: ")
        print()
        if choice == '1':
            advisor_instance.view_advisor_requests()
        elif choice == '2':
            advisor_instance.send_advisor_response()
        elif choice == '3':
            advisor_instance.view_examiner_requests()
        elif choice == '4':
            advisor_instance.send_examiners_response()
        elif choice == '5':
            advisor_instance.modify_project()
        elif choice == '6':
            advisor_instance.approve_project()
        elif choice == '7':
            break
        else:
            print("\nInvalid choice. Please try again.")
# see and do lead related activities

# once everything is done, make a call to the exit function
exit()
