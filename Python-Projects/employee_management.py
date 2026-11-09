employees = []

print("================================")
print(" EMPLOYEE MANAGEMENT SYSTEM")
print("================================")


# 1. Add Employee
def add_employee():
    print("\n--- Add Employee ---")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Employee Salary: ")

    employee = {
        "ID": emp_id,
        "Name": name,
        "Salary": salary
    }

    employees.append(employee)

    print("\nEmployee Added Successfully!")


# 2. View Employees
def view_employees():
    print("\n--- Employee Details ---")

    if len(employees) == 0:
        print("No Employees Found")
    else:
        for employee in employees:
            print("\nEmployee ID:", employee["ID"])
            print("Employee Name:", employee["Name"])
            print("Employee Salary:", employee["Salary"])
            print("------------------------")


# 3. Search Employee
def search_employee():
    print("\n--- Search Employee ---")

    search_id = input("Enter Employee ID to Search: ")

    for employee in employees:
        print("Checking Employee:", employee)

        if employee["ID"] == search_id:
            print("\nEmployee Found!")
            print("Employee ID:", employee["ID"])
            print("Employee Name:", employee["Name"])
            print("Employee Salary:", employee["Salary"])
            return

    print("Employee Not Found")
    # 4. Update Employee
def update_employee():
    print("\n--- Update Employee ---")

    update_id = input("Enter Employee ID to Update: ")

    for employee in employees:
        if employee["ID"] == update_id:

            print("Employee Found!")

            new_name = input("Enter New Employee Name: ")
            new_salary = input("Enter New Salary: ")

            employee["Name"] = new_name
            employee["Salary"] = new_salary

            print("\nEmployee Updated Successfully!")
            return

    print("Employee Not Found")
    # 5. Delete Employee
def delete_employee():
    print("\n--- Delete Employee ---")

    delete_id = input("Enter Employee ID to Delete: ")

    for employee in employees:
        if employee["ID"] == delete_id:
            employees.remove(employee)
            print("\nEmployee Deleted Successfully!")
            return

    print("Employee Not Found")


# Main Program
add_employee()

view_employees()

search_employee()

update_employee()

delete_employee()


print("\nThank you for using Employee Management System!")