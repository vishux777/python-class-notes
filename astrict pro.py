n=int(input("Enter rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j==n) or (i==n) or (j==(n-(i-1))) or ():
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()