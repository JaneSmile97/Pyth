p=raw_input()
p=list(p)
b=[]
for c in p:
    d=chr(ord(c)+3)
    b.append(d)
e="".join(b)
print(e)
