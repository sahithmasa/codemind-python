n=int(input())
m=int(input())
sum=0
for i in range(0,n):
    a=list(map(int,input().split()))
    for j in range(0,m):
        sum+=a[j]
print(sum)        