# Final project for 2023's 01219114/115 Programming I
## Senior project managing program

### CSV Files
1. `Advisor_pending_request.csv`
2. `Examiner_pending_request.csv`
3. `Member_pending_request.csv`
4. `project.csv`
5. `project_evaluations.csv`
6. `login.csv`
7. `persons.csv`

### Python Files
1. `project_manage.py`
   Contains 7 classes:
   - **class Student**: Display all project membership invitations sent to the student and allow responses and propose a new project and automatically become its Lead.
   - **class Lead**: View and manage project status, info, and requests.
   - **class Member**: View project status, responses to requests and manage project info.
   - **class Faculty**: Handle examiner and advisor requests, and respond to invitations.
   - **class Advisor(Faculty)**: Modify and approve/deny projects.
   - **class Examiners(Faculty)**: Approve/deny, give comment and evaluate projects.
   - **class Admin**: Manage projects, view or send examiner invites, change project statuses, and delete projects.

2. `database.py` 
   Contains 2 classes:
   - **class DB**: Handle table creation, addition, searching, and exporting to CSV.
   - **class Table**: Perform data manipulation, information retrieval, and table operations.

## Compilation and Execution

To get started with the Senior Project Managing Program, follow these steps to compile and run the application on your system.

### Prerequisites
- Python 3.x: Ensure Python 3.x is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
- Git: If you want to clone the repository, make sure Git is installed. You can get it from [git-scm.com](https://git-scm.com/downloads).

### Setup and Execution

1. **Clone the Repository**:  
   If you have Git installed, you can clone the repository directly. Otherwise, you can download the zip file from the GitHub repository and extract it.
   ```bash
   git clone https://github.com/colarrbear/final_project.git
   cd final_project


## Detailed Role-Based Actions

For a comprehensive overview of each role and the corresponding actions within our project, please refer to the external table. This table provides a detailed breakdown of roles, actions they can perform, associated methods, and relevant classes within the project. 

## Role-Based Actions and Completion Status

| Role     | Action                         | Method                        | Class           | Completion Percentage |
|----------|--------------------------------|-------------------------------|-----------------|-----------------------|
| Lead     | View Project Status            | `see_project_status()`        | Lead            | 100%                  |
| Lead     | Modify/View Project Info       | `modify_project_info()`       | Lead            | 100%                  |
| Lead     | View Responses to Requests     | `view_responses_to_requests()`| Lead            | 100%                  |
| Lead     | Send Request to Member         | `send_request_to_member()`    | Lead            | 100%                  |
| Lead     | Send Request to Advisor        | `send_request_to_advisor()`   | Lead            | 100%                  |
| Lead     | Exit (save changes to database)| `exit()`                      | -               | 100%                  |
| Member   | View Project Status            | `see_project_status()`        | Member          | 100%                  |
| Member   | Modify/View Project Info       | `modify_project_info()`       | Member          | 100%                  |
| Member   | View Responses to Requests     | `view_responses_to_requests()`| Member          | 100%                  |
| Member   | Exit (save changes to database)| `exit()`                      | -               | 100%                  |
| Student  | View Pending Requests          | `view_requests()`             | Student         | 100%                  |
| Student  | Accept or Deny Requests        | `handle_requests()`           | Student         | 100%                  |
| Student  | Create project                 | `change_to_lead()`            | Student         | 100%                  |
| Student  | Exit (save changes to database)| `exit()`                      | -               | 100%                  |
| Admin    | Send Invite to Examiners       | `send_invite()`               | Admin           | 100%                  |
| Admin    | Change Project Status          | `change_project_status()`     | Admin           | 100%                  |
| Admin    | Delete Project                 | `delete_project()`            | Admin           | 100%                  |
| Admin    | Display all project information| `display_all_project()`       | Admin           | 100%                  |
| Admin    | View all examiners invite      | `view_all_invites()`          | Admin           | 100%                  |
| Admin    | Delete examiners Invite        | `delete_invite()`             | Admin           | 100%                  |
| Faculty  | View Examiner Requests         | `view_examiner_requests()`    | Faculty         | 100%                  |
| Faculty  | View Advisor Requests          | `view_advisor_requests()`     | Faculty         | 100%                  |
| Faculty  | Accept/Deny Examiner Invite    | `accept_deny_examiners_invite()` | Faculty     | 100%                  |
| Faculty  | Accept/Deny Advisor Invite     | `accept_deny_advisor_request()`| Faculty       | 100%                  |
| Advisor  | Modify Project                 | `modify_project()`            | Advisor(Faculty)| 100%                  |
| Advisor  | Approve Project                | `approve_project()`           | Advisor(Faculty)| 100%                  |
| Examiner | Approve/Deny Project           | `send_project_response()`     | Examiner(Faculty)| 100%                 |
| Examiner | Evaluate Project               | `evaluate_project()`          | Examiner(Faculty)| 100%                 |


## Missing Features and Known Bugs

This section outlines the current limitations and known issues in the Senior Project Managing Program. Identifying these elements is crucial for future development and enhancements.

### Missing Features

1. **Advisor Comments on Projects**
   - **Role**: Advisor
   - **Expected Action**: Advisors should be able to leave comments or feedback on projects.
   - **Status**: This feature is currently not implemented. Advisors can view and approve projects but cannot add comments directly within the system.

2. **Admin Collects Evaluations and Communicates with Lead Students**
   - **Role**: Admin
   - **Expected Action**: Admins should collect evaluations from examiners and relay this information back to the lead students.
   - **Status**: Presently, the system lacks the functionality for admins to aggregate examiner evaluations and communicate these results to students.

### Known Bugs

1. **Inconsistent Project Status**
   - **Description**: Discrepancies in project status may occur within the database.
   - **Impact**: Affects data integrity and may lead to confusion in tracking project progress.

2. **Lead Role: Member ID Input Restriction**
   - **Description**: The system requires member IDs to be either integers or floats, which may not always be practical or possible.
   - **Impact**: Limits the flexibility in managing member information and might cause input errors.

3. **Advisor Role Limitations**
   - **Description**: Advisors have limited access to project details, hindering their ability to provide comprehensive feedback.
   - **Impact**: Affects the advisor's role in guiding and assessing projects.

4. **Admin Communication with Lead Students**
   - **Description**: No direct communication channel within the system for admins to relay feedback to lead students.
   - **Impact**: Lead students may miss out on timely and detailed feedback.

### Future Development

- Addressing these issues is a priority for the next development cycle.
- Suggestions/comments are welcome.
