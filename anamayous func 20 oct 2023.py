'''SI=lambda p,r,t:p*r*t/100
p=100
r=8
t=2
print("SI",SI(p,r,t))'''

'''THE map(f,sequence) function applies a function f to each element of a sequence 
and returns a transfored list.'''

li=[1,2,3]
def nul(x):
    return(x*2)

result=map(nul,li)
print(list(result))
