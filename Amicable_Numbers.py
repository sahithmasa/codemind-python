def div(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
m=int(input())
n=int(input())
f=div(m)
g=div(n)
if f==n and g==m:
    print("Amicable")
else:
    print("Not Amicable")