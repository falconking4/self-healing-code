def get_age(data):
    # Attempt to access 'age' key in the dictionary
    age = data["age"]
    print("Age:", age)

# Sample data dictionary without 'age' key
data = {
    "name": "Eric Johnson",
    "occupation": "Engineer"
}

if __name__ == "__main__":
    get_age(data)