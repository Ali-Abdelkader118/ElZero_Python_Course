#First
class Game:
    def __init__(self, name, developer, year , price):
        self.name = name
        self.developer = developer 
        self.year = year
        self.price = price
    def price_in_pounds(self) :
        return f"{self.price * 15.6} Egyptian Pounds"

game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}")


#Second
class User:
    def __init__(self , fname, lname, age, gender) :
        self.fname = fname
        self.lname = lname[0]
        self.age = age
        self.gender = gender
    def full_details(self) :
        if self.gender == "Male" :
            return f"Hello Mr {self.fname} {self.lname}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"
        elif self.gender == "Female" :
                return f"Hello Mrs {self.fname} {self.lname}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())
print(user_two.full_details())


#Third
class Message:

    def print_message() :
        return "Hello From Class Message"


print(Message.print_message())


#Fourth
class Games:
    def __init__(self, games):
            self.games=games
    def show_games(self) :
        if type(self.games) == int :
            print(f"I Have {self.games} Game")
        elif type(self.games) == list :
            print("I Have Many Games:")
            for i in self.games :
                print(f"-- {i}")
        else:
            print(f"I Have One Game Called {self.games}")

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()

my_games_names.show_games()

my_games_count.show_games()


#Fifth
class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"


class Admins(Members):
    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"


class Moderators(Admins):
    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"
member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())


print(member_two.show_info())


#Sixth
class A:

    def __init__(self, one):

        self.one = one

class B:

    def __init__(self, two):

        self.two = two

class C:

    def __init__(self, three):

        self.three = three

class Text(A ,B ,C) :
    def __init__(self, one , two , three):
        self.one = one 
        self.two = two 
        self.three = three
    
    def show_name(self) :
        return f"The Name Is {self.one}{self.two}{self.three}"

the_name = Text("El", "ze", "ro")

print(the_name.show_name())
