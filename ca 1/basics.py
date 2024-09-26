n=input("Enter the value: ")
for r in range (len(n)):
    for m in range(0,r+1):
        print(n[m],end="")
    print()