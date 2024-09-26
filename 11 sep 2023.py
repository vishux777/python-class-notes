n=int(input("Enter Limt : "))
m=1
sum=0
while(m<=n):
    sum=sum+m
    m=m+1
    if sum%2==0:
        print("Sum is:",sum)