n=input()
a='0123456789'
s=0
for i in n:
    if i in a:
        i=int(i)
        s=s+i
print(s)