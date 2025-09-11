#print numbers in reverse
''''n=int(input())
a=[int(input()) for i in range(n)]
for i in range(n-1,-1,-1):
    print(a[i],end=" ")'''
#sum of even numbers up to n
'''n=int(input())
a=[int(input()) for i in range(n)]
count=0
for i in range(n):
    if(a[i]%2==0):
        count=count+a[i]
print(count)'''
#count no.of digits
'''n=int(input())
a=[int(input()) for i in range(n)]
count=0
for i in range(n):
    count=count+1
print(count)'''
#factorial of a number
'''a=int(input())
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)'''
#skip multiple of 3
'''n=int(input())
a=[int(input()) for i in range(n)]
for i in range(n):
    if a[i]%3==0:
        continue
    print(a[i],end=" ")'''
#stop when negative number is found
'''n=int(input())
a=[int(input()) for i in range(n)]
for i in range(n):
    if a[i]<0:
        break
    print(a[i],end=" ")'''
#pattern
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''
#if number is neg pass
'''n=int(input())
a=[int(input()) for i in range(n)]
for i in range(n):
    if a[i]<0:
        pass
    print(a[i])'''
#numbers 1to 100
'''for i in range(1,101):
    print(i)'''
#reverse a number
'''a=input()
temp=a
rev=0
while int(a)!=0:
    rem=int(a)%10
    rev=rev*10+rem
    a=int(a)/10
print(rev)'''
#sum of even and odd numbers
'''n=int(input())
a=list(map(int,input().split(",")))
esum=0
ecount=0
osum=0
ocount=0
for i in range(n):
    if a[i]%2==0:
        esum=esum+a[i]
        ecount+=1
    else:
        osum=osum+a[i]
        ocount+=1
print(esum)
print(ecount)
print(osum)
print(ocount)'''
#fibonocii
'''n=int(input())
a=0
b=1
print(a,end="")
for i in range(1,n):
    a,b=b,a+b'''

    print(a,end=" ")
