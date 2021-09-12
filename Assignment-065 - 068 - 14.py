import os
# First
num = 1

while num <= 50:
    if num == 25:
        file = open("D:\Python\Python-14\special-text.txt", "w")
    else:
        file = open(fr"D:\Python\Python-14\text{str(num)}.txt", "w")
        file.write(f"Elzero Web School => {num}")
    num += 1
    file.close()

print(os.getcwd())      # Current Working Directory
print(os.path.dirname(os.path.abspath(__file__)))      # The Path of My Folder
print(os.path.basename(file.name))
print(num)

print("=" * 40)
# Second
file = open(r"D:\Python\Python-14\text1.txt", "a")

file.write("\n Appended => Elzero Web School " * 50)
file.close()

# Third
text_file = open(r"D:\Python\Python-14\text1.txt", "r")
number_of_lines = 0
number_of_words = 0
number_of_characters = 0
num_of_l = 0
for line in text_file :
    line = line.strip("\n")
    words = line.split()
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(line)
    if words =="l":
        num_of_l +=1


def letter_counter(letter) :
    text_file = open(r"D:\Python\Python-14\text1.txt", "r")
    text =text_file.read()
    return text.count(letter)

text_file.close()

print(f"Number Of Lines Is => {number_of_lines}")
print(f"Number Of Words Is => {number_of_words}")
print(f"Number Of Chars Is => {number_of_characters}")
print(f"Number Of \"l\" Char Is => {letter_counter('l')}")


text_file.close()

print("=" * 40)
# Fourth
for num4 in range(41, 51):
    os.remove(fr"D:\Python\Python-14\text{num4}.txt")
