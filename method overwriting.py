'''class vehicle:
    def __int__(self,name):
        self.n=name
    def getdetails(self):
        print("name",self.n)
class bus(vehicle):
    def __int__(self,model,color):
        self.model=model
        self.c=color
    def getbus(self):
        print("color:",self.c)
        print("model:",self.model)
b1=bus("volvo","red")
b1.getbus()
'''
# -----------for declaring an private -----------------------------------
class student:
    name="python"
    __age=23
    def getdata(self):
        print("Name:",self.name)
        print("Age:",self.__age)
s1=student()
s1.getdata()