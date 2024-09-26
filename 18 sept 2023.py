#find factors of  a number
n=int(input("Enter the number: "))
factors=[]
#-----------------------------------------------------------------------------------------------------------------------------------------
for i in range(1,n):
    if n%i==0:
        factors.append(i)  
 #--------------------------------------#way to print in a list.-----------------------------------------------------------------------------------
print(factors)
if sum(factors) ==n:
    print("It,s a perfect no.")
else:
    print("It,s not a perfect no.")
