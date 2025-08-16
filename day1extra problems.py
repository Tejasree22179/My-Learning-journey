'''NOTE: programs are commented in triple quotes for easy indivial testing
uncomment the quotes to run it'''
#digital clock conversion
'''seconds=int(input())
hours=seconds//3600
remaining_seconds=seconds%3600
minute=remaining_seconds//60
second=remaining_seconds%60
print(hours,"h",minute,"mm",second,"ss")'''
#Atm withdram simulation
'''amountwithdraw=int(input())
balance=int(input())
if amountwithdraw<=balance*100 and balance>500:
    balance=balance-amountwithdraw
    print(abs(balance))
else:
    print("insufficient amount")'''
#3numbers closest to target
'''input1=int(input())
input2=int(input())
input3=int(input())
target=int(input())
#which number is closest to the target it should be printed
a=target-input1
b=target-input2
c=target-input3
if a<b and a<c:
    print(input1,"it is closest")
elif b<a and b<c:
    print(input2,"it is closest")
else:
    print(input3,"it is closest")'''
#4.Average marks
'''n=int(input("enter no.of subjects"))
input1=list(map(int,input().split(",")))
a=0
for i in range(n):
    a+=input1[i]
print(a//n)'''
#5.sum of digits until single digit
'''a=int(input())
sum1=1+((a-1)%9)
print(sum1)'''
#6.electricity bill
'''units=int(input())
if units<=100:
    print("Free")
elif units>100 and units<=300:
    bill=5*units
    print(bill)
elif units>300:
    bill=10*units
    print(bill)'''
#7.triangle finder
'''side1=int(input())
side2=int(input())
side3=int(input())
if side1==side2==side3:
    print("equilateral triangle")
elif side1==side2!=side3:
    print("Issosless triangle")
elif side1!=side2!=side3:
    print("scalen triangle")'''






