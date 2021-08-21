import os
#First
num = 1


while num <= 50 :
    if num == 25 :
        file = open("D:\Python\Python-14\special-text.txt" , "w")
    else :
        file = open(fr"D:\Python\Python-14\text{str(num)}.txt" , "w")
        file.write(f"Elzero Web School => {num}")
    num +=1
    file.close()
    
print(os.getcwd())      # Current Working Directory
print(os.path.dirname(os.path.abspath(__file__)))      # The Path of My Folder
print(os.path.basename(file.name))  
#Second 
file = open(r"D:\Python\Python-14\text1.txt" , "a")

file.write("\nAppended => Elzero Web School \n" * 50)


#Third


#Fourth
for num4 in range(41 ,51) :
    os.remove(fr"D:\Python\Python-14\text{num4}.txt")
