def fac(n):
    if n==1:
        return n
    else:
        return (n*fac(n-1))
n=int(input())
for i in range(n):
    x=int(input())
    f=fac(x)
    print(f)
