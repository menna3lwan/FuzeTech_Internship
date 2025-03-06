class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.projects = []

    def update_info(self, name=None, position=None, salary=None):
        if name:
            self.name = name
        if position:
            self.position = position
        if salary:
            self.salary = salary

    def assign_project(self, project_id):
        self.projects.append(project_id)

    def remove_project(self, project_id):
        if project_id in self.projects:
            self.projects.remove(project_id)

    def get_details(self):
        return {
            'ID': self.emp_id,
            'Name': self.name,
            'Position': self.position,
            'Salary': self.salary,
            'Projects': self.projects
        }