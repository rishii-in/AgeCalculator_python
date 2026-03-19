from datetime import datetime 
print('')
print("------------Age Calculator 💡---------------")
print("")
name=input("Enter your Name 😙: ")
bday=input("Enter birth date (dd-mm-yyyy) 🎂 : ")

bday=datetime.strptime(bday,"%d-%m-%Y")

today=datetime.today()

years=today.year-bday.year
months=today.month-bday.month
days=today.day-bday.day

if days<0:
    months-=1
    days+=30
if months<0:
    years-=1
    months+=12
print("")
print(f"NAME : {name}")
print(f"AGE : {years} years {months} months {days} days ")
print("")
if years>18:
    print("Your are Minor 😊")
else:
    print("Your Adult 😜")

print("")
print("-----------------------------------------")
