#First
values = (0, 1, 2)

if any(values):
    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    print("Good")
else:
    print("Bad")
#Good

#Second
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

#Third

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

    print("Good")

# Output => Good

#Fourth
def my_all(args):
    index = 0
    for num in args:
        if bool(num) == True:
            index += 1
    if index == len(args):
        return True

    return False


print(my_all([1, 2, 3]))
print(my_all([1, 2, 3, []]))
print(my_all((1, 2, 3)))
print(my_all((1, 2, 3, [])))


def my_any(args):
    index = 0
    for i in args:
        if bool(i) == True:
            index += 1
    if index > 0:
        return True
    return False


print(my_any([0, 1, [], False]))
print(my_any([(), 0, False]))
print(my_any((0, 1, [], False)))
print(my_any(((), 0, False)))


def my_min(args):
    my_list = list(args)
    num = 0
    min_num = my_list[0]
    while num < len(my_list):
        if my_list[num] < min_num:
            min_num = my_list[num]
        num += 1
    return min_num

print(my_min([10, 100, -20, -100, 50]))
print(my_min((10, 100, -20, -100, 50)))


def my_max(args):
    my_list = list(args)
    num = 0
    max_num = my_list[0]
    while num < len(my_list):
        if my_list[num] > max_num:
            max_num = my_list[num]
        num += 1
    return max_num

print(my_max([10, 100, -20, -100, 50, 700]))
print(my_max((10, 100, -20, -100, 50, 700)))