vowels= str(input("Enter the string to count vowels:"))
count=0
for i in vowels:
    if i in "aeiouAEIOU":
        count+=1

print("The number of vowels in the string is:",count)
