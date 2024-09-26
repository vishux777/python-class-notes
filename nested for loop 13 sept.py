n=int(input("Enter the no: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print()

height=5
for row in range(1,height+1):
    print(" "*(height-row) + "+" *row)