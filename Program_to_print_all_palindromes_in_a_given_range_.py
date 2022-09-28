def pali(n):
    rev=0
    n1=n
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    if n1==rev:
        return rev
m=int(input())
n=int(input())
for i in range(m,n+1):
    if pali(i):
        print(i,end=' ')
