'''dict1={"name":"python",'age':5,"address":'Gurugram'}
print('dictionary:',dict1)
print("Name is:",dict1["name"])
a=input("data1: ")
b=input("data2: ")
list1=a.split(',')
list2=b.split(',')
dict2=dict(zip(list1,list2))
print(dict2)

dict1["contact"]=1234567
print(dict1)
print(dict1.pop('age'))
print(dict1)
print(dict1.popitem())
print(dict1)
print(dict1.clear())
del dict1
dict1.update(dict1)
print("Update",dict1)'''

#disjoint in sets is that if something is common or not in an set element or not
set1={1,2,3,4,5}
print(set1)
set2={1,2,3,1,4}
set2.add(8)
print(set2)

set2=set1.union(set2)
print(set2)
set2=set1.intersection(set2)
print(set2)
print(len(set2))
print(set2.isdisjoint(set1))#disjoint is something common or not
print(set2.issubset(set1))
print([i for i in range(1,10)])
x=[i*2 if i%2==0 else i*3 for i in range(1,11)]
print(x)

#enumearte is used to find something in a code-----------------------------------
dict3={k:"python" for k in "name"}
print(list:enumerate(list2))