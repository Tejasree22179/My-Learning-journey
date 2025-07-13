#conditional statement
#1.take 3 numbers from the user and print the greatest
'''a=int(input("enter the 1 st number"))
b=int(input("enter the 2 nd number"))
c=int(input("enter the 3 rd number"))
if a>b and a>c:
    print(f"{a} is the biggest number")
elif b>a and b>c:
    print("{} is the biggest number".format(b))
else:
    print("{} is the biggest number".format(c))'''
#2.ask the user for their age if age is<13 'child',age is between13 to 19 teen otherwise adult
'''age=int(input("enter the age"))
if age<13:
    print("child")
elif age>=13 and age<19:
    print("Teen")
else:
    print("Adult")'''
#3.to check number is divisible by 3  and 5
'''number=int(input("enter a number"))
if number%5==0 and number%3==0:
    print("divisible")
else:
    print("not divisile")'''
#4.odd or even number finding
'''a=int(input("enter a number"))
if a%2==0:
    print("the given number {} even".format(a))
else:
    print("the given number {} odd".format(a))'''
#5.check if a given character is vowel and consonant
'''a=input("enter the character")
b=a.lower()
if b=='a'or b=='e' or b=='i' or b=='o'or b=='u':
    print("the given character is a vowel")
else:
    print("the given character is a consonant")'''
#6.create a grade system 90+=A,80-89=B,70-79=c,<70=D
'''marks=int(input("enter the marks"))
if marks>=90:
    print("Grade A")
elif marks>80 and marks<=89:
    print("Grade B")
elif marks>70 and marks<=79:
    print("Grade c")
else:
    print("Grade D")'''
#given year is a leap year or not
'''year=int(input("enter the year"))
if year%4==0:
    if year%100!=0 or year%400==0:
        print("the given year is a leap year")
    else:
        print("the given year is a not an leap year")'''
#check if a person is eligible for vote
'''age=int(input("enter the age"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")'''
#----------------------------- LOOPS-------------------------------------------------
#print all numbers from 1 to 100
'''for i in range(1,101):
    print(i)'''
#print even numbers between 1 to 50
'''for i in range(2,51,2):
    print(i)'''
#print multiplication
'''table=int(input("enter a number"))
for i in range(1,11):
    print(table*i)'''
#print factorial
'''number=int(input("enter the number"))
fact=1
for i in range(1,number+1):
    fact=fact*i
print(fact)'''
#fibonocci series upto n terms
'''n=int(input("enter a number"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b'''
#count the digits in a given number
'''number=int(input("enter the number"))
digit=0
for i in range(number+1):
    if number==0:
        pass
    else:
        number=number//10
        digit+=1
print(digit)'''
#reverse a given number using a loop
'''number=int(input("enter a number"))
result=0
while number!=0:
    rem=number%10
    result=result*10+rem
    number=number//10
print(result)'''
#reverse a given string using a loop
'''number=input("enter a number")
result=""
for char in number:
    print(char)
    result=char+result
print(result)'''
#sum of digits in a number
'''number=int(input("enter a number"))
sums=0
while number!=0:
    rem=number%10
    sums=sums+rem
    number=number//10
print(sums)'''
#pattern
'''rows=int(input("enter the number of rows"))
for i in range(1,rows+1):
    print("*"*i)'''
#prime numbers between 1 to 100
'''number=int(input("enter the end number"))
count=0
for i in range(2,number+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        count+=1
print(count)'''
#count number of digits
'''number=int(input("enter a number"))
count=0
while number!=0:
    rem=number%10
    count+=1
    number=number//10
print(count)'''
#-----------------------------------FUNCTION----------------------------------------
#define a function to check wheather a number is even or odd
'''def evenorodd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
number=int(input("enter a number"))
print(evenorodd(number))'''
#factorial of a number
'''def fact(number):
    if number==0 or number==1:
        return 1
    else:
        return number*fact(number-1)
number=int(input("enter a number"))
print(fact(number))'''
#given string is palindrome or not
'''def palindrome(number):
    result=""
    for i in number:
        result=i+result
        print(result)
number=input("enter the string")
print(palindrome(number))'''
#average of 3 averages
'''def average(number1,number2,number3):
    print((number1+number2+number3)//3)
number1=int(input("enter the number"))
number2=int(input("enter the number"))
number3=int(input("enter the number"))
average(number1,number2,number3)'''
#prints multiplication tables from 1 to 10
'''def multiplication(*args):
    for num in args:
        print(f"the table is {num}")
        for i in range(1,11):
            print(num*i)
multiplication(1,2,3,4,5,6,7,8,9,10)'''
#reverse a string
'''def reverse(number):
    result=""
    for i in number:
        result=i+result
    print(result)
number=input("enter a number")
reverse(number)'''
#function that counts the words in a sentence
'''def word(sentence):
    words=sentence.split()
    print(words)
    count=0
    for word in words:
        count+=1
    print(count)
sentence=input("enter a sentence")
word(sentence)'''
#function that returns all vowels in a string
'''def vowels(strings):
    a=strings.lower()
    for i in a:
        if i=='a' or i=='e'or i=='i'or i=='o' or i=='u':
            print(i,end=",")

strings=input()
vowels(strings)'''
#function that returns that sum of all digits in a number
'''def sumofdigit(number):
    sums=0
    while number!=0:
        rem=number%10
        sums=sums+rem
        number=number//10
    print(sums)
number=int(input("enter a number"))
sumofdigit(number)'''
#check if a number is prime
'''def prime(number):
    count=0
    for i in range(1,number+1):
        if(number%i==0):
            count+=1
    if(count>2):
        print("it is not prime")
    else:
        print("it is a prime")
number=int(input("enter a number"))
prime(number)'''

#armstrong number
'''def armstrong(number):
    temp=number
    sums=0
    while number!=0:
        rem=number%10
        sums=sums+rem**3
        number=number//10
    if(sums==temp):
        print("Armstrong number")
    else:
        print("not armstrong number")
number=int(input("enter a number"))
armstrong(number)'''
#loop prints only numbers divisible by both 2 and 3 from 1 to 100
'''number=int(input("ebter a number"))
for i in range(1,101):
        if i%2==0 and i%3==0:
            print(i)'''
#log in page verification using if and else
current_username="Tejasree"
current_password="Teju@123"
username=input()
password=input()
if username==current_username and password==current_password:
    print("login successfull")
else:
    print("login failed")
    
    

    
    
