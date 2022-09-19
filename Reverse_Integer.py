n=int(input())
s=0
c=0
if n<0:
    n=n*-1
    c+=1
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if c==1:
    print(-s)
else:
    print(s)