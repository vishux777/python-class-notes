'''"take name and marks as input from user. Until the entered marks is "end" print the marks
a=str(input("Enter Name: "))
while (a!="end"):
    b=int(input("Enter Marks:"))
    print(a,"scored",b,"marks.")
    
    a=str(input("Enter Name: "))
else:
    print("You Entered End.")'''
'''----------------------------------------------------------------------------------------------------'''
name=input("Enter Input: ")
while(name!="end"):
    if name.isdigit(c):
        print("it is integer.")
else:
    list1 =list(name)
    i=0
    f=0
    while i<len(list1):

        if list1[1]=="." or list1[i].isdigit():
            i=i+1
        else :
            f=1
            break#used to break the while loop.---------------------------------------------
if f==1:
    print("it is string")

else:
    print("it is float")
name=input("enter input: ")