#First


def remove(letters) :

    return letters[1 : -1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
friends_cleaned = map(remove , friends_map)
for friend in friends_cleaned : 
    print(friend)

print("=" *40)


# def remove2(letters2) :

#     return letters2[1:-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
for friend in map(lambda letter: letter[1:-1] , friends_map) : 
    print(friend)


print("=" *40)

#Second
def get_names(name):
    return name.endswith("m")

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)

for friend in names:
    print(friend)

print("=" *40)

for fr in filter(lambda name : name.endswith("m") ,friends_filter) :
    print(fr)

print("=" *40)

#Third
nums = [2, 4, 6, 2]

def multiply(nums) :
    total = 1
    for num in nums:
        total *= num
    return total

print(multiply(nums))

print("=" *40)

#Fourth
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

skills_counter = enumerate(reversed(list(skills)) ,50)

for c ,s in skills_counter :
    if type(s) == int :
        continue
    else:
        print(f"{c} - {s}")

print("=" *40)


skills_list = list(skills)
skills_list.reverse()
counter = 50

for skill in skills_list :
    if type(skill) == int :
        continue
    else :
        print(f"{counter} - {skill}")
        counter += 1