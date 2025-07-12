'''NOTE: programs are commented in triple quotes for easy indivial testing
uncomment the quotes to run it'''
#caluculator program
'''def caluculate(number1,number2,operation):
    if operation=="add":
        print(number1+number2)
    elif operation=="sub":
        print(number1-number2)
    elif operation=="mul":
        print(number1*number2)
    elif operation=="div":
        print(number1/number2)
    elif operation=="pow":
        print(number1**number2)
    elif operation=="flordiv":
        print(number1//number2)
    else:
        print(number1%number2)
number1=int(input())
number2=int(input())
operation=input()
caluculate(number1,number2,operation)'''
#Temperature convertor-->take temperature in celsius convert it into the fahrenheit
"""celsius=float(input("enter the temperature in celsius"))
fahrenheit=(celsius*9/5)+32
print("the fahrenheit value is {}".format(fahrenheit))"""
#caluculate the simple interest
'''principal=int(input("enter the principal element"))
rate=float(input("enter the rate"))
time=float(input("enter the time"))
simple_intrest=(principal*time*rate)/100
print(f"the value of simple intrest is{simple_intrest}")'''
#square and cube of a given number
'''number=int(input("enter a number"))
print("the square and cube of a given number is {} and {}".format(number**2,number**3))'''
#check wheather a given number is positive,negative,or zero
'''number=int(input("enter the number"))
if number>0:
    print(f"the given number is positive")
elif number==0:
    print(f"the given number is zero")
else:
    print("the given number is negative")'''
#age caluculator--> enter the birth year and caluculate the current age
"""birth_year=int(input("enter birth year"))
current_year=int(input("enter the current year"))
age=current_year-birth_year
print("the age is {}".format(age))"""
#datatype identifier-->take a input as a value print its data type and print its value
'''name="tejasree"
print(f"my name is {name} and type is {type(name)}")'''
#minutes to hours ex:135 minutes convert into hours
'''minutes=int(input("enter the minutes"))
hours=minutes/60
print(f"the toatal hours is{hours}")'''
#compound intrest
'''principal=int(input("enter the amount"))
rate=int(input("enter the rate"))
time=int(input("enter the time"))
amount=(principal*(1+rate/100)**time)
compound_intrest=amount-principal
print(f"the compound intrest is {compound_intrest}")'''
#swaping of 2 number
'''a=int(input("enter any number"))
b=int(input("enter a number"))
temp=a
a=b
b=temp
print("after swapping",a,b)'''










