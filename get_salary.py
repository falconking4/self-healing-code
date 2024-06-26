def get_salary(employee_data):
    if 'salary' in employee_data:
        salary = employee_data['salary']
        print('Salary:', salary)
    else:
        print('Salary not found')

if __name__ == '__main__':
    employee_data = {
        'name': 'Mark Thompson',
        'position': 'Software Developer'
    }
    
    get_salary(employee_data)
