n=int(input("Enter a number: "))
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return(n * fact(n-1))
if n<=0:
    print("Majak mat kar yaar")
else:
    print("Factorial:",fact(n))