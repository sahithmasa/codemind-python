n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    i=str(i)
    k=len(i)
    l.append(k)
for i in l:
    if i==max(l):
        c+=1
print(c)