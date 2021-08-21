#First
from typing import Counter


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends [0])
print(friends.pop(0))
print(friends [-1])
print(friends.pop(-1))
#second
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0::2])
print(friends[1::2])
#Third
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(f"\" {friends[1]} \" , \" {friends[2]}\" , \"{friends[3]}\",")
print(f"\" {friends[-2]} \" , \" {friends[-1]}\"")
#Fourth
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-1] ="Ali118"
friends[-2] ="Ali118"
print(friends)
#Fifth
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends.append("Philo")
friends.insert(0 , "Adham")
print(friends)
#Sixth
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.remove("Osama")
friends.remove("Nasser")
print(friends)
friends.remove("Salem")
print(friends)
#Seventh
friends = ["Ahmed", "Philo"]
employees = ["Youssef", "Ziad"]
school = ["Adham", "Remon"]
friends.extend(employees)
friends.extend(school)
print(friends)
#Eighth
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
#Nine
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
#Ten
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])
