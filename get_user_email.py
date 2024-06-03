def get_user_email(user_info):
    email = user_info["email"]
    print("User email:", email)

user_info = {
    "user_name": "Bob Johnson",
    "user_id": 101
}

if __name__ == "__main__":
    get_user_email(user_info)
