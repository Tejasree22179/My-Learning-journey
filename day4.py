'''NOTE: programs are commented in triple quotes for easy indivial testing
uncomment the quotes to run it'''
#Types of list creation
'''list1=[1,2,3,4]
print(list1)'''
#user defined
'''list1=list(map(int,input().split(" ")))
print(list1)'''
#task 1- create a list of 5 subjects you study
'''subjects=input().split(" ")
#print(subjects)'''
#length of list
'''print(len(subjects))'''
#2.Add 2 more subjects to list using insert and append
'''subjects.append("Webdevelopment")
subjects.insert(5,"advancedmaths")
print(f" after inserting web\n {subjects}")
print(f" after inserting advancemaths\n {subjects}")'''
#3.remove a subject not to study
'''subjects.remove("operatingsystem")
subjects.pop()
print("subjects after removing os\n{}".format(subjects))
print("subjects after removing 5 th element \n {}".format(subjects))'''
#4.change 2 element
'''subjects[2]="web development"
print(subjects)'''
#5.print subjects one by one
'''list2=["os","cn","maths","webdevelopment","python","ai","ml"]
n=len(list2)
for i in range(n):
    print(list2[i])'''
#6.sort list alphabetically and then reverse  them
'''list2=["os","cn","maths","webdevelopment","python","ai","ml"]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)'''
#7.check if maths is present in the list or not
'''list2=["os","cn","maths","webdevelopment","python","ai","ml"]
if "maths" in list2:
    print("found")
else:
    print("not found")'''
#8.create a list of numbers and find the max,min,and sum
'''list3=[398498,838,89938,9803,8974,40,9328,90283,930,984,75,53,3553,354,45,53]
print(max(list3))
print(min(list3))
print(sum(list3))'''
#9.count the number of times a value occurs
'''list4=["teja","teju","sunny","teja","teja","teja"]
print(list4.count("teja"))'''
#10.using index extract the value
'''list4=["teja","teju","sunny","teja","teja","teja"]
print(list4[2:6])'''
#------------------------------- TUPLES------------------------------------------
#1.create a tuple with 4 seasons
"""tuple1=tuple((input().split(" ")))
print(tuple1)"""
#2.accesing first and last elements
"""tuple1=tuple((input().split(" ")))
print(tuple1[0])
print(tuple1[-1])"""
#3.changing the tuple value lets see what type of error will get
# change is done when we convert it into the list if we will not change into the list it will through an error
"""tuple1=tuple((input().split(" ")))
tuple1=list(tuple1)
tuple1[3]="cold season"
print(tuple(tuple1))"""
#4.check if winter exists or not in that
"""tuple1=tuple((input().split(" ")))
if "winter" in tuple1:
    print("found")
else:
    print("not found")"""
#5.loop tuple print all the items
'''tuple1=tuple((input().split(" ")))
for i in tuple1:
    print(i)'''
#6.create a tuple with 5 numbers and find the average
'''tuple1=tuple(map(int,input().split(" ")))
sum1=0
for i in range(len(tuple1)):
    sum1+=tuple1[i]
print(sum1)
print(sum1//len(tuple1))'''
#7.convert list into tuple",
'''list4=[1,2,3,4,5]
tuple4=tuple(list4)
print(tuple4)'''
#8.create a nested tuple
tuple5=tuple(("teja","sunny",("Kajal","prudhvi",("Darshini","yashmi")),"vishnu"))
print(tuple5)

             
