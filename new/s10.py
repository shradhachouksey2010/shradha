age =float(input("enter your age:"))
if age>=18: 
    print("you can vote")
    print("thanks for visit")

age =float(input("enter your age:"))
if age>=18:
    print("you can vote")
else:
    print("you can't vote")
print("thanks for visit")

number =int(input("enter any number"))
if number%2==0:
    print("given number is even:")
else:
    print("given number is'nt even")

x=10
print(str(x))
print(list(x))
print(type(x))
y=str(x)
print(list(y))
print(tuple(y))


age=int(input("enter your age:"))
if 0<=age<18:
   print("your age is under 18")
elif 18<=age<60:
   print("your age in between 18 to 60")
elif age>=60:   
   print ("you are senior citizen")
else:
   print("please enter valid age") 
year = int(input("Enter a year: "))

  
# LEAP YEAR

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year.") 

year= int(input("enter any year"))
if year %400==0 or year%4==0 and year%100!=0:
   print(f'given year{year}is leap year') 
else:
   print(f"given year{year}is not a leep year")

   
