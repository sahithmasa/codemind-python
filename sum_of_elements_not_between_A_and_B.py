n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in m:
    if a>i or b<i:
        s+=i
print(s)
    