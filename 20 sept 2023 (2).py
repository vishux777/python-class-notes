number = int(input("Enter Number: "))
number_string = str(number)
length = len(number_string)
print(length)
sum=0
for i in range(0,1):
    b=number
    sum+=sum+b**1
print("Sum:",sum)
if (int(number)==sum):
    print("It's an armstrong")    
else:
    print("Not an armstrong")