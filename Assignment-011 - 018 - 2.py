name="'Ali'"
name2="Ali"
age='"16"'
age2=16
country="Egypt"
#First
print("\"Hello " + name + "," + " How You Doing \\ " + "\"\"\"" + " Your Age Is " + age + "\"" + " +" + " And Your Country Is :" + country)
#Second
print("\"Hello " + name + "," + " How You Doing \\ " + "\n" + "\"\"\"" + " Your Age Is " + age + "\"" + " +" + "\n" + " And Your Country Is :" + country)
#Third
name1="Ali118"
print("Second Letter Is \"" + name1[1] + "\"" + "\n" +"Third Letter Is \"" + name1[2] + "\"" + "\n" +"Last Letter Is \""+name1[-1] + "\"")
#Fourth
print(name1[1:4])
print(name1[0::2])
name = "Ali118" [::-2]
print(name)
#Fifth
name2="@#@#@#Ali118@#@#@#"
print(name1.strip("@#"))
#Sixth
num = "9"
num1 = "15"
num2 = "130"
num3 = "950"
num4 = "1500"
print(num.zfill(4))
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
#Seventh
name_two="Ali-Mohamed"
print(name1.rjust( 20 , "@"))
print(name_two.rjust( 20 , "@"))
#Eighth
name_3="MOHameD"
name_4="mohAMEd"
print(name_3.swapcase())
print(name_4.swapcase())
#Ninth
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
#Ten
print(name1.rfind("i"))
#Eleven
msg_2 = "I <3 Python And Although <3 Elzero Web School"
print(msg_2.replace("<3" , "Love" , 1))
#Twelve
print(msg_2.replace("<3" , "Love"))
#Thirteen
print("My Name Is {:s} , And My Age Is {:d} , And My Country Is {:s} " .format(name2 , age2 , country ))
