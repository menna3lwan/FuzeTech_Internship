class Project:
    def __init__(self, project_id, name, budget, deadline):
        self.project_id = project_id
        self.name = name
        self.budget = budget
        self.deadline = deadline
        self.employees = []

    def assign_employee(self, emp_id):
        self.employees.append(emp_id)

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees.remove(emp_id)

    def update_budget(self, budget):
        self.budget = budget

    def update_deadline(self, deadline):
        self.deadline = deadline

    def get_project_details(self):
        return {
            'ID': self.project_id,
            'Name': self.name,
            'Budget': self.budget,
            'Deadline': self.deadline,
            'Employees': self.employees
        }