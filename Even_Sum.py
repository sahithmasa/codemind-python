n=int(input())
a=list(map(int,input().split()))
se=0
for i in range(0,n):
    if a[i]%2==0:
        se+=a[i]
print(se)        