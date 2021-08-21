#First
tuple1 = "Ali" ,
print(tuple1)
print(type(tuple1))
#Second
friends = ("Ali" , "Philo" , "Ahmed")
friends1 = list(friends)
friends1[0] = "Ali118"
friends =tuple(friends1)
print(friends)
print(type(friends))
print(len(friends))
#Third
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters = nums + letters
print(nums_and_letters)
print(len(nums_and_letters))
#Fourth
my_tuple = (1, 2, 3, 4)
a , b , _ , c = my_tuple
print(a)
print(b)
print(c)
