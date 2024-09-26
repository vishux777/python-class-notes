'''
def fun1():
    global a
    a=6
def fun2():
    a=7
a=5
print("a initially:",a)
fun1()
print("a after fun1:",a)
fun2()
print("a after fun2:",a)

#----------------------------------------------------------------------------------------------------
def sub(a,b):
    print(a,b)
sub(5,4)
sub(a=5,b=4)
sub(a=4,b=5)
'''

def welcome(name,message):
    print(message,name)
n=input("name: ")
m=input("message: ")

welcome(name=n,message=m)
welcome(n,message=m)
welcome(message=m,name=n)