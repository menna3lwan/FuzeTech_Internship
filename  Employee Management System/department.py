class Department:
    def __init__(self, dept_id, name, manager_id=None):
        self.dept_id = dept_id
        self.name = name
        self.manager_id = manager_id
        self.employees = []

    def assign_manager(self, manager_id):
        self.manager_id = manager_id

    def add_employee(self, emp_id):
        self.employees.append(emp_id)

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees.remove(emp_id)

    def get_department_details(self):
        return {
            'ID': self.dept_id,
            'Name': self.name,
            'Manager': self.manager_id,
            'Employees': self.employees
        }