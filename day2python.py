'''NOTE: programs are commented in triple quotes for easy indivial testing
uncomment the quotes to run it'''
'''rows=int(input())
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print()'''
#Swap Two Variables Without Using a Third Variable or Arithmetic Operators
'''a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a,b)'''
#2.Reverse a String Without Slicing or Built-in Functions,Input: "Python",Output: "nohtyP"
'''a=input()
rev=""
for i in a:
    rev=i+rev
print(rev,end="")'''

#1. Swap Two Numbers Without a Temporary Variable

#Take two integers as input and swap them without using a third variable.
'''a=int(input())
b=int(input())
a,b=b,a
print(a,b)'''
#2. Sum of Digits of a Number

#Write a program to read a number and print the sum of its digits.,Example: Input: 253 → Output: 10
'''a=input()
summ=0
for i in a:
    summ+=int(i)
print(summ)'''
#3. Check Data Type of User Input,Accept an input and display its data type.

#Extend it: If input is numeric, print square of the number, otherwise print "Not a number".
'''a=int(input())
if type(a)==int:
    print(a**2)
else:
    print("Not a number")'''
#4. Reverse a String

#Take a string as input and reverse it without using slicing ([::-1]).
''''a=input()
rev=""
for i in a:
    rev=i+rev
print(rev)'''
#5. Calculate Simple Interest

#Take principal, rate of interest, and time as input and calculate Simple Interest = (P × R × T) / 100
'''
    si=(p*t*r)/100

'''
#6. Convert Celsius to Fahrenheit and Vice Versa

#Input temperature and convert from Celsius → Fahrenheit or Fahrenheit → Celsius based on user's choice.
'''c=(f-32)*5/9
(c*9/5)+32=f'''
#7. Find the ASCII Value of a Characte
#Take a character as input and print its ASCII value.
'''a='y'
print(ord(a))
b=int(input())
print(chr(b))'''

#8. Check if a Number is Positive, Negative, or Zero,Input a number and print:,"Positive" if number > 0

#"Negative" if number < 0 ,"Zero" otherwise.
'''number =int(input())
if number<0:
    print("-ve")
elif number>0:
    print("+ve")
else:
    print("0")'''
#9. Count the Number of Vowels in a String

#Input a string and count how many vowels it contains (a, e, i, o, u).
'''number=input()
number=number.lower()
count=0
for i in number:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)'''

#10. Area and Perimeter of a Rectangle

#Input length and breadth and calculate area & perimeter.
'''area=l*b
perimeter=1/2*b*h'''
