### `Student` Role Methods

1. **view_requests**: This method should display all the project membership invitations sent to the student. It filters the requests where the student is listed as a potential member (`to_be_member`) and shows details such as project ID, response, and response date.

2. **handle_requests**: This method enables the student to respond to project invitations. It presents the student with pending requests and allows them to accept or deny each one.

3. **change_to_lead**: Allows a student to take on the role of a project lead. This method might involve updating the project table to set the student as the lead for a specific project.

### `Admin` Role Methods

1. **send_invite**: This method is for sending invitations to faculty members to become examiners for projects. It likely involves updating an examiners table with new entries for each invite.

2. **change_project_status**: Used to update the status of a project, such as from 'ongoing' to 'completed'. It involves modifying the project's record in the project table.

3. **delete_project**: Allows for the removal of a project from the project table.

4. **display_all_project**: This function should list all projects in the project table, showing details like project ID, title, members, advisor, and status.

5. **view_all_invites**: Used to view all sent examiner invitations. It might involve fetching and displaying data from an examiner invites table.

6. **delete_invite**: This method is for deleting an examiner invite, possibly from an examiner invites table.

### `Faculty` Role Methods

1. **view_examiner_requests**: Shows all requests for the faculty member to become an examiner for various projects.

2. **view_advisor_requests**: Displays requests for the faculty member to act as an advisor for projects.

3. **accept_deny_examiners_invite**: Allows the faculty member to accept or deny examiner invitations.

4. **accept_deny_advisor_request**: Enables the faculty member to accept or deny requests to be an advisor.

5. **advisor**: Check if the current faculty member is an advisor for any project. If they are, they should be able to perform advisor-specific tasks.

6. **examiner**: check if the current faculty member is an examiner for any project. If they are, they should be able to perform examiner-specific tasks.

### `Advisor` and `Examiners` Specific Methods

1. **modify_project (Advisor)**: Allows an advisor to make changes to the details of a project they are advising.

2. **approve_project (Advisor)**: Used by an advisor to approve a project.

3. **send_project_response (Examiners)**: Allows an examiner to send their response or feedback on a project.

4. **evaluate_project (Examiners)**: Used by examiners to evaluate and provide a detailed assessment of a project.
