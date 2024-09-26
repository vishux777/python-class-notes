import re
pattern=r"[6-9][0-9]{9}"
string="Welcome 6667778889 dsf fasdf 9876543210"
repl="hello"
phones=re.sub(pattern,repl,string)
print(phones)