n=input()
a='0123456789'
c=0
for i in n:
    if i in a:
        c+=1
if c==0:
    print("Doesn't contain digit" )
else:
    print('Contains',c,'digit')