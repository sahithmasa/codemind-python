n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in a:
    i=str(i)
    k=len(i)
    l.append(k)
for i in l:
    if i==min(l):
        c+=1
print(c)