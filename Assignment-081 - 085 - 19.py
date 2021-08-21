#First 


def reverse_string(my_string):

    yield my_string[::-1]


for c in reverse_string("Elzero"):
    print(c)


print("=" * 40)

#Second


def my_decorator(func) :
    def decoration() :
        print("Sugar Added From Decorators")

        func()

        print("#" * 40)

    return decoration


@my_decorator
def make_tea():
    print("Tea Created")


@my_decorator
def make_coffee():
    print("Coffee Created")


make_tea()
make_coffee()
