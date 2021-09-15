from typing import final
from PIL import Image

"""
This Is My Solved Assignment For ElZero.com
"""

#First

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    for dt in data :
        my_data.append(dt.lower())



def listToString(s): 

    str1 = "" 
    
    return (str1.join(s))

final_string = listToString(my_data).capitalize()

print(final_string)

print("=" * 40)

#Second
# Still Solving

print("=" * 40)

#Third
image = Image.open("elzero-pillow.png")

l_box = (400, 0, 800, 400)
new_l = image.crop(l_box)

converted_l = new_l.convert("L")

onverted_l.show()
converted_l.save("converted_l.png")


coulmn_box = (0, 400 , 1200 , 800)
new_box = image.crop(coulmn_box)

converted = new_box.convert("L")
rotated= converted.rotate(180)

rotated.show()
rotated.save("Rotated-image.png")


# #Fourth
def Say_Hello(name) :
    '''
    "parameter(someone) => Person Name"
    "Function To Say Hello To Anyone"
    '''
    print(f"Hello {name}")

Say_Hello("Ali")
print(Say_Hello.__doc__)

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
