def get_user_email(user_info):
    if 'email' in user_info:
        email = user_info['email']
    else:
        email = None
    return email