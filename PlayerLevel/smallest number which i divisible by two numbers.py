try:
    a = int(input())
    b = int(input())
    z=max(a,b)
    x=z
    y = min(a,b)
    while(x%y!=0):
        x+=z
    print(x)    
except:
    print("Invalid Input")
