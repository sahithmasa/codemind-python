def palin(n):
    a=n[::-1]
    if a==n:
        return 1
    else:
        return 0
n=input().lower()
n=n.split()
c=0
for i in n:
    if palin(i):
        c+=1
print(c)