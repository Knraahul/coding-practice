Fizzbuzz= int(input("Enter the number from 1- 100 :"))
if Fizzbuzz % 3 ==0 and Fizzbuzz % 5 ==0:
    print("FizzBuzz")
elif Fizzbuzz %3==0:
    print("Fizz")
elif Fizzbuzz %5==0:
    print("Buzz")  
elif Fizzbuzz >=1 and Fizzbuzz <=100:
    print(Fizzbuzz)    
else:
    print("Enter the number between 1-100:")
    exit()          