n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i>=0:
        i=str(i)
        k=len(i)
        l.append(k)
    else:
        i=str(i)
        j=len(i)
        l.append(j-1)
print(*l)