n=int(input())
l=list(map(int,input().split()))
se=so=0
for i in range(0,n):
    if i%2==0:
        se+=l[i]
for i in range(0,n):
    if i%2!=0:
        so+=l[i]
if se>so:
    print(se-so)
else:
    print(so-se)
