n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in m:
    if a>i or b<i:
        c+=1
        print(i,end=' ')
if c==0:
    print("-1")
