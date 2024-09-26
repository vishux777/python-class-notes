f=open("aest.txt","w")
a=input("Enter Text: ")
f.write(a)
f.close()
f=open("aest.txt","r")
print(f.read(5))
print(f.readlines())
#firstly opened it in write mode and then in read mode.'''

f=open("aest.txt","a")
f.write("hello")
print(f.tell())