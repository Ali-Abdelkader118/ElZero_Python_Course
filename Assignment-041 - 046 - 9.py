#First
num1 = int(input("Enter Your First Number  ").strip())
operation =input("Enter Your Operation  ").strip()
num2 = int(input("Enter Your Second Number  ").strip())
if operation == "/" :
    print(f"Your Result Is : { num1 + num2}")
elif operation == "-" :
    print(f"Your Result Is : { num1 - num2}")
elif operation == "*" :
    print(f"Your Result Is : { num1 * num2}")
elif operation == "+" :
    print(f"Your Result Is : { num1 + num2}")
elif operation == "%" :
    print(f"Your Result Is : { num1 % num2}")
else :
    print("Sorry Your Operation Is not Supported")
print("=" * 50)
#Second
age = int(input("Enter Your Age  "))
if age > 16 : print("App Is Suitable For You")
else : print("App Is Not Suitable For You")
print("=" * 50)
#Third
age = int(input("Please Enter Your Age  "))
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
Seconds = minutes * 60
if 10 < age < 100 :
    print(f"Your Age In Months Is {months}")
    print(f"Your Age In Weeks Is {weeks}")
    print(f"Your Age In Days Is {days}")
    print(f"Your Age In Hours Is {hours}")
    print(f"Your Age In Minutes Is {minutes}")
    print(f"Your Age In Seconds Is {Seconds}")
else :
    print("Sorry Your Age Is Not Supported")
print("=" * 50)
#Fourth
country = input("Input Your Country  ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries :
    price = price - discount
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price}")
else :
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
print("=" * 50)
