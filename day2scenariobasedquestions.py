'''NOTE: programs are commented in triple quotes for easy indivial testing
uncomment the quotes to run it'''
number=int(input())
if number%3==0 and number%5==0:
    print("FizzBuzz")
elif number%3==0:
    print("Fizz")
elif number%5==0:
    print("Buzz")
else:
    print("number is ",number)
