#First
num1 = int(input("Enter Your Number  "))
my_list =[]
if num1 > 0:
    while num1 > 1:
        num1 -= 1
        if num1 == 6 : 
            continue
        elif num1 == 0 : break 
        print(num1)
        my_list.append(num1)
    print(f"{len(my_list)} Numbers Printed Successfully.")
else:
    print("Your Number Can't Be Less Than 0")
#Second
friends = ["Ali", "Philo", "ahmed", "Adham", "remon"]
ignored = []
num3 = 0
friends.sort()
print(friends)
while len(friends) > 2 :
    print(friends[num3])
    del(friends[num3])
    num =+ 1
else :
    print(f"Friends Printed And Ignored Names Count Is {len(friends)}" )
#Third
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
num4 = 0
while len(skills) > 0 : print(skills[num4]) ; del(skills[num4]) ; num =+ 1
#Fourth
my_friends =[]
maxfriends = 5

while maxfriends > 0:
    name = input("Please Enter Your Name  ").strip()
    if name.isupper():
        print("Invalid Name")
    elif name.islower() :
        name.capitalize()
        my_friends.append(name.capitalize())
        maxfriends -= 1
        print(f"Friend {name.capitalize()} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {maxfriends}")
        print(my_friends)
    else:
        my_friends.append(name)
        maxfriends -= 1
        print(f"Friend {name} Added")
        print(f"Names Left in List Is {maxfriends}")
        print(my_friends)
else:
    print("Names Is Full , You Cant Add more") 
if len(my_friends) > 0:
    my_friends.sort()
    index = 0
    print("Printing The List Of Names")

    while index < len(my_friends) :
        print(my_friends[index])
        index += 1
