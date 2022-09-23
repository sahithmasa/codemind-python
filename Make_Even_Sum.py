n=int(input())
k=list(map(int,input().split()))
o=0
e=0
for i in range(n):
    if k[i]%2==0:
        e+=1
    else:
        o+=1
if o%2==0:
    print(1)
else:
    print(0)
    
