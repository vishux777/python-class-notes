#global and local variables
'''def fun1():
    a=5
    print("value of a inside fun1:",a)
a=int(input("enter a: "))
print("Initial a:",a)
fun1()
print("Value of a after funnction call:",a)


#new
'''
def fun1(a):
    a=a+1
    print("a inside fun1:",a)
    return(a)
    
def fun2(a):
    print("a times 2",a*2)

a=int(input("Enter a: "))
print("Initial a:",a)
fun1(a)
print("Value of a after function call:",a)
fun2(a)
