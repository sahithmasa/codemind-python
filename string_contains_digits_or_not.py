n=int(input())
for i in range(n):
    b=input()
    a='0123456789'
    for i in b:
        if i in a:
            print('Yes')
            break
    else:
        print('No')