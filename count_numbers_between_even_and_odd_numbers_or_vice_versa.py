n=int(input())
a=list(map(int,input().split()))
x=0
for i in range(0,n-2):
    if ((a[i]%2==0 and a[i+2]%2)or(a[i]%2 and a[i+2]%2)):
        x+=1
print(x)        