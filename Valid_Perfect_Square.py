def ps(n):
    for i in range(1,n):
        if n==i*i:
            print(True)
            break
    else:
        print(False)
n=int(input())
for i in range(n):
    x=int(input())
    ps(x)