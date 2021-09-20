#First

NUM = input("Add Your Number: ")

if NUM.isalpha():
    raise Exception("Only Numbers Allowed")
elif len(NUM) >= 2 :
    raise IndexError("Only One Character Allowed")
elif int(NUM) <= 0 :
    raise ValueError("Number Must Be Larger Than 0")
else:
    print("#" * 20)
    print(f"The Number Is {NUM}")
    print("#" * 20)


#Second
letter = str(input("Add Letter From A to Z : "))

try:
    if (len(letter) >= 2 , letter.isalpha()== True) :
        print(f"You Typed {letter}")
    else :
        if len(letter) >= 2 :
            raise IndexError
        elif letter.isalpha() == False:
            raise TypeError

except TypeError:
    print("The Letter Not In A - Z")
except IndexError:
    print("You Must Write One Character Only")

#Third

def calculate(num1, num2) -> int:
    return num1 + num2

print(calculate(20, 30))
