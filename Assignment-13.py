#First
def ranks(**skills) :
    for skill_key , skill_value in skills.items() :
        print(f"{skill_key} => {skill_value}")
        
ranks(css = "90" , html = "100")

print("=" * 40)
#Second
def ranks(name="" ,**skills) :
    if len(name) == 0 :
        for skill_key , skill_value in skills.items() :
            print(f"{skill_key} => {skill_value}")
    elif len(skills) ==0 :
        print(f"Hello {name.capitalize()} You Have No Scores To Show")
    else :
        print(f"Hello {name.capitalize()} This Is Your Score Table:")
        for skill_key , skill_value in skills.items() :
            print(f"{skill_key} => {skill_value}")
        
ranks(css ="50" , html = "100")

print("=" * 40)
#Third
scores_list = {
    "Math": "90",
    "Science": "80",
    "Language": "70"
}

def scores(name="" ,**scores) :
    if len(name) == 0 :
        for  score_key , score_value in scores.items() :
            print(f"{score_key} => {score_value}")
    elif len(scores) ==0 :
        print(f"Hello {name.capitalize()} You Have No Scores To Show")
    else :
        print(f"Hello {name.capitalize()} This Is Your Score Table:")
        for score_key , score_value in scores.items() :
            print(f"{score_key} => {score_value}")
        

scores(**scores_list )