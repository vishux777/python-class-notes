a=int(input("Enter a number: "))
flag=0
for i in range(2,a):
    if (a%i==0):
        print("It's not prime number")
        flag=1
        break

if (flag==0):
        print("prime")


#method2-----------------------------------------------------------------------------------
