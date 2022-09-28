def pali(n):
    rev=0
    k=n
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    if rev==k:
        print(True)
    else:
        print(False)
n=int(input())
for i in range(n):
    x=int(input())
    pali(x)