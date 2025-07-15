#Note:
'''- Each program is marked with a heading in comments.
- All are inside multiline comments for easy testing.
- Uncomment one block at a time when running.'''
#greatest elements on the right
'''arr=list(map(int,input().split()))
n=len(arr)
greatest=0
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            break
        else:
            greatest+=1
print(greatest)'''
#2.addition using args i/p-10,20,30 ,o/p=60
'''def add(*number):
    c=len(number)
    sums=0
    for i in range(c):
        sums=sums+number[i]
    print(sums)
add(10,20,30)''' #o/p=60
#3.display user details like name ,age,course
'''def user(**details):
    print(details)
user(name="Tejasree",age="20",course="python")'''
'''o/p={'name': 'Tejasree', 'age': '20', 'course': 'python'}'''
#3.Program: Greet with a default name If no name is given, greet 'User'
'''def greet(name="user"):
    print("hello", name)
greet()
greet("tejasee")
greet("welcome to python world")''' #o/p=hello user/n ,hello tejasee/n,hello welcome to python world
#4.Program: Lambda to calculate square of a number Input: 6 Output: 36
'''square=lambda x:x**2
print(square(6))''' #0/p=36
#5.Program: Lambda to check if number is even Input: 7, Output: False
'''even=lambda x:x%2==0
print(even(7))'''#o/p=False
#6.Program: Use map() to square numbers Input: [1, 2, 3]  Output: [1, 4, 9]
'''inputs=[1,2,3]
square=list(map(lambda x:x**2,inputs))
print(square)''' #o/p=[1, 4, 9]
#7.Program: Use filter() to keep even numbers Input: [1, 2, 3, 4] Output: [2, 4]
'''inputs=[1,2,3,4]
even=list(filter(lambda x:x%2==0,inputs))
print(even)''' #o/p:[2, 4]
#8.Program: Use reduce() to find sum of list Input: [5, 10, 15] ,Output: 30
'''from functools import reduce
sums=reduce(lambda x,y:x+y,[5,10,15])
print(sums)''' #o/p:30
#9.Program: Double each value using lambda + map() Input: [2, 4, 6],Output: [4, 8, 12]
'''inputs=[2,4,6]
double=list(map(lambda x:x**2,inputs))
print(double)''' #o/p=[4, 16, 36]
#10.Program: Filter numbers > 10 Input: [5, 12, 7, 20],Output: [12, 20]
'''inputs=[5,12,7,20]
number=list(filter(lambda x:x>10,inputs))
print(number)''' #o/p=[12, 20]





