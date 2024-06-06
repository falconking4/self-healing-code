def get_age(data):
    # Check if 'age' key exists before accessing
    if 'age' in data:
        age = data['age']
        print('Age:', age)
    else:
        print('Age not provided')

# Sample data dictionary without 'age' key
data = {
    'name': 'Eric Johnson',
    'occupation': 'Engineer'
}

if __name__ == '__main__':
    get_age(data)
