# Final project for 2023's 0219114/115 Programming I
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
1. **project_manage.py**  
   Contains 7 classes:
   - **class Student**: Display all project membership invitations sent to the student and allow responses.
   - **class Lead**: Manage project status, info, and requests.
   - **class Member**: View project status and responses to requests.
   - **class Faculty**: Handle examiner and advisor requests, and respond to invitations.
   - **class Advisor (Faculty)**: Modify and approve projects.
   - **class Examiners (Faculty)**: Approve/deny and evaluate projects.
   - **class Admin**: Manage projects, send examiner invites, change project statuses, and delete projects.

2. **database.py**  
   Contains 2 classes:
   - **class DB**: Handle table creation, addition, searching, and exporting to CSV.
   - **class Table**: Perform data manipulation, information retrieval, and table operations.
