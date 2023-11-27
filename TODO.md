# Programming I: Final Project

This project has 7 classes:

--- 

## 1. Person():

Attribute: 
- person_type(str)
- person_ID(str)
- person_first(str)
- person_last(str)

## 2. Admin(Person):

Attribute: 
- person_type(str): admin
- person_ID(str)
- person_first(str)
- person_last(str)

Method:
- modify_table()

## 3. Student(Person):

Attribute: 
- person_type(str): student
- person_ID(str)
- person_first(str)
- person_last(str)

Method:
- view_pending_requests()
- accept_deny_request(): member_pending_request table, project_table table needs to be updated
- change_to_lead(): must deny all member request first, project_table table, login table needs to be updated
- view_project()
- modify_project()

## 4. Lead(Person):

Attribute: 
- person_type(str): lead
- person_ID(str)
- person_first(str)
- person_last(str)

Method: 
- project_status()
- modify_project(): project table needs to be updated
- request_status()
- send_member_request()
- send_advisor_request(): advisor_pending_request table needs to be updated
- submit_project()

## 5. Member(Person):

Attribute: 
- person_type(str): member
- person_ID(str)
- person_first(str)
- person_last(str)

Method: 
- project_status()
- modify_project(): project table needs to be updated
- request_status()

## 6. Faculty(Person) -- Normal Faculty Role which is not an advisor:

Attribute: 
- person_type(str): faculty
- person_ID(str)
- person_first(str)
- person_last(str)

Method: 
- view_supervisor_request()
- send_accept_advisor_response()
- send_deny_advisor_response()
- view_project_details(): working with project table
- evaluate_project(): (details in proposal)

## 7. Advising_Faculty(Faculty):

Method: 
- view_supervisor_request()
- send_accept_advisor_response()
- send_deny_advisor_response()
- view_project_details(): working with project table
- evaluate_projects(): (details in proposal)
- approve_project()
