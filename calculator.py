def add(a,b):
    a=a+b
    print("Answer:",a)
def  sub(a,b):
    a=a-b
    print("Answer:",a)
def div(a,b):
    a=a/b
    print("Answer",a)
def mul(a,b):
    a=a*b
    print("Answer",a)

a=int(input("First Number: "))
b=int(input("Second Number: "))
c=input("What you want to do:")
if c=="+" or c=="Addition":
    add(a,b)   
elif c=="-" or c=="Substraction":
    sub(a,b)   
elif c=="*" or c=="Multiplication":
    mul(a,b)
elif c=="/" or c=="Division":
    div(a,b)
else:
    print("Sorry not compactable with this till now.")
