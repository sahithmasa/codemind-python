n=input()
a=input()
c=0
for i in n:
    if i in a:
        c+=1
if c==0:
    print('-1')
else:
    print(c)