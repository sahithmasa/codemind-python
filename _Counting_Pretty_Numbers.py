t=int(input())
for i in range(t):
    a=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        k=l%10
        l+=1
        if k==2 or k==3 or k==9:
            a+=1
    print(a)        