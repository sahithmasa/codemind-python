a,b=map(int,input().split())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    if i>=0:
        i=str(i)
        k=len(i)
        l.append(k)
    else:
        i=str(i)
        j=len(i)
        l.append(j-1)
for i in l:
    if i==b:
        c+=1
print(c)