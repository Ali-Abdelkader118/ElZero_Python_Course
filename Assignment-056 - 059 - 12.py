#First
def calculate(n1 , n2 , sign="multiply") :
    if sign.lower() == "add" or sign == "a":
        print(n1 + n2)
    elif sign.lower() == "subtract" or sign == "s" :
        print(n1 - n2)
    elif sign.lower() == "multiply" or sign == "m" :
        print(n1 * n2)
    else:
        print("The Operation Is Wrong")        

calculate(10, 20 , "m")
#Second
def addition(*num) :
    n = 0
    for num2 in num :
        if num2 == 5 :
            n -= 10
        elif num2 == 10: 
            n -= 10
        n += num2
    print(n)
addition(10 , 15 ,20 ,30 ,5 ,40)

#Third
def show_skills(name , *skills) :
    if len(skills) == 0 :
        print(f"Hello {name} You Have No Skills")
    else :
        print(f"Hello {name.capitalize()} Your Skills Is : ")
        for skill in skills :
            print(f"-- {skill}")

show_skills("Ali" , "JS" , "HTML" , "CSS" , "Python")

#Fourth
def say_hello(name="Unknown" , age="Unknown" , country="Unknown") :
    print(f"Hello {name.capitalize()} Your Age Is {age} And You Live In {country.capitalize()}")


say_hello("ali" , 17 , "Egypt")
