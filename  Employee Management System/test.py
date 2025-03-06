from employee import Employee
from department import Department
from project import Project
from hr_system import HRSystem

hr_system = HRSystem()

employee_1 = Employee(1, "Ali", "Software Engineer", 15000)
employee_2 = Employee(2, "Mona", "Data Scientist", 18000)
employee_3 = Employee(3, "Kareem", "Project Manager", 25000)

hr_system.add_employee(employee_1)
hr_system.add_employee(employee_2)
hr_system.add_employee(employee_3)

engineering_dept = Department(101, "Engineering")
data_science_dept = Department(102, "Data Science")

hr_system.add_department(engineering_dept)
hr_system.add_department(data_science_dept)

engineering_dept.assign_manager(employee_1.emp_id)
data_science_dept.assign_manager(employee_2.emp_id)

engineering_dept.add_employee(employee_1.emp_id)
engineering_dept.add_employee(employee_3.emp_id)
data_science_dept.add_employee(employee_2.emp_id)

ai_chatbot_project = Project(201, "AI Chatbot", 50000, "30-Apr-2025")
ecommerce_platform_project = Project(202, "E-commerce Platform", 75000, "15-May-2025")

hr_system.add_project(ai_chatbot_project)
hr_system.add_project(ecommerce_platform_project)

ai_chatbot_project.assign_employee(employee_1.emp_id)
ai_chatbot_project.assign_employee(employee_2.emp_id)
ecommerce_platform_project.assign_employee(employee_3.emp_id)

employee_1.assign_project(ai_chatbot_project.project_id)
employee_2.assign_project(ai_chatbot_project.project_id)
employee_3.assign_project(ecommerce_platform_project.project_id)

print("\n--- Employees ---")
for employee in hr_system.employees:
    print(employee.get_details())

print("\n--- Departments ---")
for department in hr_system.departments:
    print(department.get_department_details())

print("\n--- Projects ---")
for project in hr_system.projects:
    print(project.get_project_details())