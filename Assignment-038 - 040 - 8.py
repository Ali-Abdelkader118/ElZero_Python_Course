#First

name = input("What is Your Name?  ").capitalize().strip()
print(f"\"Hello {name} , Happy to See You Here\"")
print("=" * 50)

#Second

age = input("What is Your Age ?  ")
agereq = 16

if int(age) > agereq :
    print(f"\"Hello Your Age Is {age} , All Articles Is Suitable For You\"")

else :
    print("\"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You\"")

print("=" * 50)

#Third

fname = input("What is Your First Name ?  ").capitalize().strip()
lname = input("What is Your Last Name ?  ").capitalize().strip()
print(f"Hello {fname} {lname[0:1]}.")
print("=" * 50)

#Fourth
email = input("Enter Your Email ").strip().lower()
print(f"Your Name Is {email [0:email.index('@')].capitalize()}")
print(f"Email Service Provider Is {email [email.index('@') + 1 : email.index('.')]}")
print(f"Top Level Domain Is {email [email.index('.') : ] }")
