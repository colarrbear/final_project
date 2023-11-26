# Project Evaluation Proposal

## Introduction:

The evaluation step is an important part of the senior project process. It allows a group of faculties to assess the quality of a submitted project report and provide feedback to the lead student. This feedback can help the lead student to improve the report before it is submitted for final approval.

## Evaluation Steps (2-5):

1. **(*)Submission Step:**
   - Lead student submit the final project report.

2. **Evaluation Step:**
   - Form the committee: should consist of at least two faculties.
   - A group of faculties evaluates the submitted report.

3. **Feedback Step:**
   - provide feedback to the lead student on the overall quality of the project report and on any specific areas that need improvement.
   - Calculate scores* (based on criteria if exist).

4. **Reviewer Assignment (recheck):**
   - Assign specific faculties to review each project.
   - Ensure a fair evaluation process.

5. **(*)Final Approval Step:**
   - The advisor approves the project after successful evaluation.

## Code Outline for Evaluation:

### In Project Class:

```python
class Project:
    def __init__(self, title, description, ...):
        # Project initialization code
    
    def calculate_score(self):
        # Calculate the overall score based on defined criteria
        pass
        
    def evaluate_report(self):
        # Form the evaluation committee
        # get the project report send to the evaluation committee
        # Collect feedback from the evaluation committee
        # Calculate the overall score
        # Provide feedback to the lead student

class Faculty:

    def evaluate_project_report(self, project):
        # Provide feedback on the project report based on established criteria
        pass


