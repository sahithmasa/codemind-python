n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=0
for i in m:
    if a>i or b<i:
        d+=1
        c.append(i)
if d==0:
    print('-1')
else:
    print(max(c))
