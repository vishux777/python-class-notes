'''def sum(* args):
    sum=0
    for i in args:
        sum=sum+1
    print("sum: ",sum)

sum(1,2,3)
sum(1,2)'''

def ln(*n):
    l=len(n)
    num=list(n)
    for i in range(0,l-1):
        if num[1]>num[i+1]:
            num[i+1]=num[i]
    print("largest",num[l-1])

ln(3,6,12,4,7)


