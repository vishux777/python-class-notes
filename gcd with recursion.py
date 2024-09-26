a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
def gcd(x,y):
    if y==0 or y==1:
        return(x)
    else:
        return(gcd(y,x%y))
print(gcd(a,b))