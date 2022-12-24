n, m = map(int,input().split())
d="-"
b=".|."
c=1
e=1
for j in range(0,n):
    if j<int(n/2):   
        print(d*(int(m/2)-c),end="")
        print(b*e,end="")
        print(d*(int(m/2)-c))
        c+=3
        e+=2
    elif j==(int(n/2)):
        print("WELCOME".center(m,"-"))
    else:
        c-=3
        e-=2
        print(d*(int(m/2)-c),end="")
        print(b*e,end="")
        print(d*(int(m/2)-c))
