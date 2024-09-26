a=(input("Enter NO.1: "))
b=(input("Enter NO.2: "))
c=(input("Enter No.3: "))
if (a<b<c):
    print("NO. 3 is greater")
else:
    if (c<b):
        print("NO. 2 is greatest")
    else:
        print("NO. 1 is Largest")

ch=input("Enter Alphabat: ")
if (ch>='a' and ch<='z'):
    print("LowerCase")
else:
    print("UpperCase")

#islower can also be used
#iisdigit can be used for checking Digit.(ch)