import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="ajay",
    password="ajay",
    database="employee"
)

def main():
    print("Welcome to Employee Management System :)\n")
    print("Press 1 to view all Employee details,")
    print("Press 2 to view details of a specific Employee,")
    print("Press 3 to add new Employee,")
    print("Press 4 to remove an Employee,")
    print("Press 5 to exit the portal\n")

    i = int(input("Enter some value: "))
    print()

    if i == 1:
        display()
    elif i == 2:
        emp_id = int(input("Enter employee id: "))
        display(emp_id)
    elif i == 3:
        name = input("Enter employee's name: ")
        age = int(input("Enter employee's age: "))
        post = input("Enter employee's post: ")
        salary = int(input("Enter employee's salary: "))
        add_employee(name, age, post, salary)
    elif i == 4:
        emp_id = int(input("Enter employee id: "))
        remove_employee(emp_id)
    elif i == 5:
        print("Good Bye :)")
        exit()
    else:
        print("Invalid input, please enter a valid number")

def check_employee(emp_id):
    cursor = db.cursor(buffered=True)
    query = f"SELECT * FROM employee_details WHERE id={emp_id}"
    cursor.execute(query)
    row = cursor.rowcount
    if row == 1:
        return True
    return False

def add_employee(name, age, post, salary):
    cursor = db.cursor()
    query = f"""INSERT INTO employee_details 
        (name, age, post, salary)
        VALUES ('{name}', {age}, '{post}', {salary})
    """
    cursor.execute(query)
    db.commit()
    print("Employee added successfully\n")

def remove_employee(emp_id):
    cursor = db.cursor()
    if check_employee(emp_id):
        query = f"DELETE FROM employee_details WHERE id={emp_id}"
        cursor.execute(query)
        db.commit()
        print("Employee removed successfully\n")
    else:
        print("Employee does not exist\n")

def display(emp_id=None):
    cursor = db.cursor()
    if emp_id is None:
        query = "SELECT * FROM employee_details"
        cursor.execute(query)
        for i in cursor:
            print(i)
    else:
        if check_employee(emp_id):
            query = f"SELECT * FROM employee_details WHERE id={emp_id}"
            cursor.execute(query)
            for i in cursor:
                print(i)
        else:
            print("Employee does not exist")
    print()

#i make some changes here
if __name__ == "__main__":
    while True:
        main()
