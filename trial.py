'''a=int(input("Enter Number: "))
class hi:
    def hello(self,a):
        if a==0 or a==1:
            return 1
        else:
            return(a*self.hello(a-1))
b=hi()
print(b.hello(a))'''

c=int(input("Enter Number: "))
d=int(input("New Value: "))
list1=[1,2,3,4,5]
class hi:
    def v(self,a,list2,d):
        self.a=a
        self.list2=list2
        self.d=d
    def p(self):
        self.list2[self.a]=self.d
        return(self.list2)
b=hi()
b.v(c,list1,d)
print(b.p())