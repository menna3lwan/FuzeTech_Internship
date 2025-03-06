class HRSystem:
    def __init__(self):
        self.employees = []
        self.departments = []
        self.projects = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_department(self, department):
        self.departments.append(department)

    def add_project(self, project):
        self.projects.append(project)