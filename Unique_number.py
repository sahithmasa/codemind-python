n=int(input())
l=[]
c=0
n1=n
while n:
    r=n%10
    c+=1
    if r not in l:
        l.append(r)
    n//=10
if c==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")
    