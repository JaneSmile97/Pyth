num=int(input())
b=[]
x=2
while(num!=1):
	if num%x==0:
		num=num//x
		b.append(x)
		x=2
	else:
		x=x+1
ans=''
for x in b:
	ans=ans+" "+str(x)
print(ans)
