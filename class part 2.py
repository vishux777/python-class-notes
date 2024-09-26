class student:
    def details(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name is:",self.name)
        print("age is:",self.age)

s1=student()
name=input("name: ")
age=input("age: ")
s1.details(name,age)
s1.show()