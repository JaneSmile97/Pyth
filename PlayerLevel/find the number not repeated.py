def cnt(str):
	(max,a)=(-1,0)
	r=[]
	for i in range(len(str)):
		if str[i] in r:
			continue
		r.append(str[i])
		for j in range(len(str)):
			if str[i]==str[j] :
				a=a+1
		if a==1:
			print(str[i])
		a=0
def main():
	try:
		n=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		cnt(l)
	except:
		print('invalid')
main()
