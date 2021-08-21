# First

print("First")
my_list = [1, 2, 3, 3, 4, 5, 1]
uniqe_list = [1, 3]
my_list.sort()
uniqe_list = set(my_list)
print(uniqe_list)
uniqe_list = list(uniqe_list)
print(type(uniqe_list))
print(uniqe_list[0:4])
print("=" * 50)

# Second

print("Second")
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
nums.add("A")
nums.add("B")
nums.add("C")
print(nums)
print("=" * 50)

# Third

print("Third")
my_set = {1, 2, 3}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")
print("=" * 50)

# Fourth

print("Fourth")
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_two.issuperset(set_one))
print("=" * 50)

# Fifth

print("Fifth")
user = {
    "HTML": "90%",
    "CSS": "90%",
    "PYTHON": "30%"
}
user.update({"AI": "20%"})
print("\"HTML Progress Is " + user.get("HTML") + "\"")
print("\"CSS Progress Is " + user.get("CSS") + "\"")
print("\"PYTHON Progress Is " + user.get("PYTHON") + "\"")
print("\"AI Progress Is " + user.get("AI") + "\"")
