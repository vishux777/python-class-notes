'''import re
pattern=r"[6-9][0-9]{9}"
string="dsafffd9876543210 jdfhdjj 9876567890"
phones=re.findall(pattern,string)
#use search in place of findall for getting only first
#result.
#use match in place of findall to find from only 
#one side.
print(phones)'''

import re
pattern=r"[6-9][0-9]{9}"
f=open("fest.txt","r+")
string=f.read()
phones=re.findall(pattern,string)
print(phones)
print(len(phones))