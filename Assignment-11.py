#First
my_nums = [15, 81, 5, 17, 20, 21, 13]
num2 = []
num3 = 0
for num in my_nums :
    if num % 5 == 0 :
        num2.append(num)
num2.sort(reverse=True)
for num in num2 :
    num3 =num3+ 1
    print(f"{num3 } => {num}")    


print("=" * 40)
#Second
num2 = 0
while num2 < 21 :
    num2 = num2 +1
    if num2 == 6 : continue
    elif num2 == 8 : continue
    elif num2 == 12: continue
    print(str(num2).zfill(2))
print("All Numbers Printed")

print("=" * 40)
#Third
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
A = 100
B =80
C = 40
for rank in my_ranks :
    if my_ranks[rank] == "A" :
        print(f"{rank} Is {my_ranks[rank]} And This Equals {A} ")
    if my_ranks[rank] == "B" :
        print(f"{rank} Is {my_ranks[rank]} And This Equals {B} ")
    if my_ranks[rank] == "C" :
        print(f"{rank} Is {my_ranks[rank]} And This Equals {C} ")


print("=" * 40)
#Fourth
students = {
    "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
},
    "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
},
    "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
}
}
A = 100
B =80
C = 40
D = 20
total_marks = 0
for rank2 in students :
    print("-" * 30)
    print(f"-- Student Name => {rank2}")
    print("-" * 30)
    for rank3 in students[rank2] :
            if students[rank2][rank3] == "A" :
                print(f"{rank2} => {A} ")
                total_marks += A
            if students[rank2][rank3]  == "B" :
                print(f"{rank2} => {B} ")
                total_marks += B
            if students[rank2][rank3]  == "C" :
                print(f"{rank2} => {C} ")
                total_marks += C
            if students[rank2][rank3]  == "D" :
                print(f"{rank2} => {D} ")
                total_marks += D
    print(f"Total Points For {rank2} Is {total_marks}")
    total_marks = 0


print("=" * 40)
#Fourth 2
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

A = 100
B = 80
C = 40
D = 20

for student_name , student_degree in students.items() :
    print("-" * 30)
    print(f"-- Student Name => {student_name}")
    print("-" * 30)
    for subject , degree in student_degree.items() :
        if degree == "A" :
            print(f"{degree} => {A} ")
            total_marks += A
        if degree  == "B" :
            print(f"{degree} => {B} ")
            total_marks += B
        if  degree == "C" :
            print(f"{degree} => {C} ")
            total_marks += C
        if degree  == "D" :
            print(f"{degree} => {D} ")
            total_marks += D
    print(f"Total Marks For {student_name} Is {total_marks}")
    total_marks = 0