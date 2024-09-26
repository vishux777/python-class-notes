class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name is",self.name)
        print("age is:",self.age)
'''s1=student()
s1.name="Python"
age=input("age: ")
s1.age=age
print("name is:",s1.name)
print("age is:",s1.age)'''

name=input("name: ")
age=input("age: ")
S1=student(name,age)
S1.show()
name1=input("name: ")
age1=input("age: ")
S2=student(name1,age1)
print("Name of second student:",S2.name)