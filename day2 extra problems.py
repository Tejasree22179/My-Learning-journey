'''NOTE: programs are commented in triple quotes for easy indivial testing
uncomment the quotes to run it'''
#1. Sum of Odd Numbers
'''Input:7(Find the sum of all odd numbers from 1 to 7.)'''
'''sum1=0
for i in range(1,8,2):
    sum1=sum1+i
print(sum1)'''
#2. Largest of Three Numbers,Input:15 22 18
'''n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 and n1>n3:
    print(f"{n1} is greater number")
elif n2>n1 and n2>n3:
    print("{} is the greatest number".format(n2))
else:
    print(n3,"is the greatest number")'''
#3.Multiplication Table Input:9
'''n1=int(input())
for i in range(1,21):
    print(i,"*",n1,"=",i*n1)'''
#4.. Factorial of a Number Input:6
'''n1=int(input())
fact=1
for i in range(1,n1):
    fact=fact*i
print(fact)'''
#5.Count Positive, Negative, and Zero ,Input:5
#-4 0 7 -1 3
'''n1=int(input())
pos=0
neg=0
zero=0
arr=[int(input()) for i in range(n1)    ]
for i in arr:
    if i>0:
        pos=pos+1
    elif i<0:
        neg=neg+1
    else:
        zero=zero+1
print("pos count",pos)
print("neg count",neg)
print("zero count",zero)'''
#6.Reverse Digits of a Number Input:12345
'''n=input()
rev=""
for i in n:
    rev=i+rev
print(rev)'''
#7.Check Armstrong NumberInput:153
'''num=input()
temp=int(num)
rev=0
c=len(num)
while int(num)!=0:
    rem=int(num)%10
    rev=rev+rem**c
    num=int(num)/10
if int(rev)==temp:
    print("Armstrong number")
else:
    print("not an armstrong number")'''
#8. Print Even Numbers Between 1 and N Input:20
'''n=int(input())
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count>2:
        print("not a prime",i)
    else:
        print(i,"is a prime")'''
#9.. Check Leap Year,Input:2028
'''year=int(input())
if year%4==0:
    if year%400==0 or year%100!=0:
        print("the given year is leap year",year)
    else:
        print("the given year is not a leap year",year)
else:
    print("the given year is not a leap year",year)'''
#10. Sum of Digits Until Single Digit,Input:9875
'''n=int(input())
while n>=10:
    sum1=0
    while n>0:
        rem=n%10
        sum1=sum1+rem
        n=n//10
print(sum1)'''
#digital root:
n=int(input())
print(1+(n-1)%9)
    



    
