def HCF(a,b):
        if a > b:
            smaller = b
        else:
            smaller = a
        for i in range(1, smaller+1):
            if((a % i == 0) and (b % i == 0)):
                hcf = i
        return hcf
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(HCF(n1, n2))
