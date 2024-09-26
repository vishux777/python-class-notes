def fib():
    n=int(input("Enter the no: "))
    a=0
    b=1
    print(a)
    while(b<=n):
        print(b)
        temp=b
        b=a+b
        a=temp
def fac():
    print("factorial")

a=input("What do you want to do: ")
if a=="fib":
    fib()
else:
    fac()