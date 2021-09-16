
"""This Is My Solved Assignment For ElZero 20th Assignment"""
from PIL import Image

#First

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    for dt in data :
        my_data.append(dt.lower())



def list_to_string(s_l):
    """This function turn list to a string"""
    str1 = ""

    return str1.join(s_l)

FINAL_STRING = list_to_string(my_data).capitalize()

print(FINAL_STRING)

print("=" * 40)

#Second
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple2 = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data2 = []

for item1, item2, item3 in zip(my_list1, my_tuple2, my_list2):
    if isinstance(item2 , int) is True :
        break
    if isinstance(item3 , int) is True :
        break
    my_data2.append(item2)
    my_data2.append(item3)

FINALL_STRING= list_to_string(my_data2).capitalize()


print(FINALL_STRING)


print("=" * 40)

#Third
image = Image.open("elzero-pillow.png")

l_box = (400, 0, 800, 400)
new_l = image.crop(l_box)

converted_l = new_l.convert("L")

# converted_l.show()
converted_l.save("converted_l.png")


coulmn_box = (0, 400 , 1200 , 800)
new_box = image.crop(coulmn_box)

converted = new_box.convert("L")
rotated= converted.rotate(180)

# rotated.show()
rotated.save("Rotated-image.png")


# #Fourth
def say_hello2(name) :
    '''
    "parameter(someone) => Person Name"
    "Function To Say Hello To Anyone"
    '''
    print(f"Hello {name}")

say_hello2("Ali")
print(say_hello2.__doc__)

print("=" * 40)

#Fifth
myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    """
    This Function Says Hello To List Of People
    """
    for some_one in some_peoples:
        print(f"Hello {some_one}")

say_hello(myFriends)
