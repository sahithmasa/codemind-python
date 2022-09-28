n=int(input())
a=list(map(int,input().split()))
se=so=0
for i in range(0,n):
    if a[i]%2==0:
        se+=a[i]
for i in range(0,n):
    if a[i]%2!=0:
        so+=a[i]
if se>so:
    print(se-so)
else:
    print(so-se)