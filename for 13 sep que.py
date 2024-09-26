n=int(input("Enter the number: "))
m=int(input("Enter the range: "))
if m<=10:
    
    for i in range(1,m+1):
        print(n,"x",i,"=",n*i)
else:
    m=10
    for i in range(1,m+1):
        print(n,"x",i,"=",n*i)

#another method-----------------------------------------------------------------------------
for i in range(1,m+1):
    print(n,"x",i,"=",n*1)
    if (i==10):
        break
    #-----------------------------------------------------------------------------------