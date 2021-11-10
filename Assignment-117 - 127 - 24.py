import sqlite3

#First

# - Date
# - Text
# - String
# - Integer
# - Float


#Second

db = sqlite3.connect("elzero.db")
cr = db.cursor()
cr.execute("CREATE TABLE if not exists Users(ID Integer UNIQUE, Name Text UNIQUE, Age Text UNIQUE, Email Text UNIQUE)")


#Third
cr.execute("INSERT OR IGNORE INTO Users(ID , Name , Age , Email) values(1 ,'Ahmed','20/10/1980','a@elzero.org')")
cr.execute("INSERT OR IGNORE INTO Users(ID , Name , Age , Email) values(2 ,'Sayed','20/10/1990','s@elzero.org')")
cr.execute("INSERT OR IGNORE INTO Users(ID , Name , Age , Email) values(3 ,'Gamal','05/10/1991','g@elzero.org')")
cr.execute("INSERT OR IGNORE INTO Users(ID , Name , Age , Email) values(4 ,'Mahmoud','09/10/1987','m@elzero.org')")
cr.execute("INSERT OR IGNORE INTO Users(ID , Name , Age , Email) values(5 ,'Sameh','08/11/2000','h@elzero.org')")



#Fourth
cr.execute("SELECT * FROM Users ORDER BY id DESC LIMIT 1")
result = cr.fetchone()
print(result)


#Fifth

id = input("Enter User ID : ")

def show_skills():
    cr.execute("SELECT * FROM Users")
    result = cr.fetchall()
    print("Show Other Data :")

    for row in result :
        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")


def delete_user(id) :
    cr.execute(f"DELETE FROM Users WHERE ID ='{id}'")
    print("User Deleted")


cr.execute("SELECT ID FROM Users")
id2 = cr.fetchall()
uid = []
for i in id2 :
    uid.append(i[0])



if id in str(uid):
    delete_user(id)
    show_skills()
else:
    print("User ID Not Found")


db.commit()
