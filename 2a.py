


#2
import re
email_cond = "^[a-z]+[a-z][0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email: ")
if re.search (email_cond, user_email):
    print("Rght Email")
else:
    print("Wrong Email")
