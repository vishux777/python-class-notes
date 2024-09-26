y= int(input("Enter a Year: "))
if (y%100 == 0 and y%400==0):
    print("Is leap")
elif(y%100 !=0 and y%4 ==0):
    print("is leap year")
else:
    print("is not leeap")