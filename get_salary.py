def get_salary(employee_data):
    salary = employee_data["salary"]
    print("Salary:", salary)

employee_data = {
    "name": "Mark Thompson",
    "position": "Software Developer"
}

if __name__ == "__main__":
    get_salary(employee_data)