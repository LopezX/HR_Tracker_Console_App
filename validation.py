import re
from email_validator import validate_email, EmailNotValidError

def valid_id():
    valid = False
    id = None
    while (not valid):
        id = input("Candidate ID (Integer, Non-negative): ")
        if not id.isdecimal():
            print("Invalid Candidate ID.\n")
        else:
            id = int(id)
            valid = True
            print()
    
    return id

def valid_first_name():
    valid = False
    first_name = None
    while (not valid):
        first_name = input("First name (cannot be blank): ")
        if not first_name.isalpha() or len(first_name) == 0:
            print("Invalid first name.\n")
        else:
            valid = True
            print()
    
    return first_name

def valid_last_name():
    valid = False
    last_name = None
    while (not valid):
        last_name = input("Last name (cannot be blank): ")
        if not last_name.isalpha() or len(last_name) == 0:
            print("Invalid last name.\n")
        else:
            valid = True
            print()
    
    return last_name

def valid_email():
    valid = False
    email = None
    while (not valid):
        email = input("Email (cannot be blank): ")
        try:
            valid_email = validate_email(email)
            email = valid_email.email
            valid = True
            print()
        except EmailNotValidError as e:
            print(str(e))
    
    return email

def valid_phone_number():
    valid = False
    phone_number = None
    while (not valid):
        phone_number = input("Phone Number (Format as ###-###-####, if none enter 000-000-0000): ")
        
        if (re.match("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", phone_number)):
            if phone_number == "000-000-0000":
                phone_number = None
            valid = True
            print()
        else:
            print("Invalid phone number.\n")
    
    return phone_number

def valid_profiles():
    valid = False
    profile = None
    while (not valid):
        print("Profiles (LinkedIn, Indeed, etc.)")
        profile = input("(if none, type \"None\"; separate each profile by a space): ")
        
        hasDigits = re.compile('\d')
        if hasDigits.search(profile):
            print("Invalid profile(s) given (cannot contain digits)\n")
        else:
            if profile == "None" or len(profile) == 0:
                profile = None
            valid = True
            print()
            
    return profile