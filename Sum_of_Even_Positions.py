n=int(input())
l=list(map(int,input().split()))
se=0
for i in range(0,n):
    if i%2==0:
        se+=l[i]
print(se)