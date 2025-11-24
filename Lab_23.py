# import re

# def validate_pan(pan):
#     pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
#     if re.match(pattern, pan):
#         return True
#     return False

# # Test the function
# pan_number = input("Enter PAN card number: ")
# if validate_pan(pan_number):
#     print("Valid PAN card number.")
# else:
#     print("Invalid PAN card number.")

# def validate_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(pattern, email):
#         return True
#     return False

# # Test the function
# email_id = input("Enter email ID: ")
# if validate_email(email_id):
#     print("Valid email ID.")
# else:
#     print("Invalid email ID.")


#------------------POST LABS---------------
import re 
 
def pan(pan): 
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$' 
    return bool(re.match(pattern, pan)) 
 
def email(email): 
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    return bool(re.match(pattern, email)) 
 
PAN = input("Enter PAN number: ") 
EMAIL = input("Enter Email ID: ") 
 
if pan(PAN): 
    print("PAN is Valid") 
else: 
    print("PAN is Invalid") 
if email(EMAIL): 
    print("Email is Valid") 
else: 
    print("Email is Invalid") 
