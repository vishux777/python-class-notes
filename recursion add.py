n=5
m=4
def add(x,y):
    if y==0:
        return x
    else:
        return x+add(1,y-1)
        #return add(x+1,y-1)------------ALTERNATE METHOD-----------------------
print(add(n,m))