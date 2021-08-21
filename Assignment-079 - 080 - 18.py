import datetime


old_date = datetime.datetime(2021, 6, 25).date()
new_date = datetime.datetime.now().date()


print(f"Days From {old_date} To {new_date} Is => {(new_date - old_date).days} Days")


print("=" *50)

#Second
date_now = datetime.datetime.now()


print(date_now.strftime("%Y-%m-%d"))
print(date_now.strftime("%b %d , %Y"))
print(date_now.strftime("%d - %b - %Y"))
print(date_now.strftime("%d / %b / %y"))
print(date_now.strftime("%d / %B / %Y"))
print(date_now.strftime("%a | %d | %B | %Y"))
