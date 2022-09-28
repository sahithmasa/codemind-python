n=input()
n=n.split()
l=[]
for i in n:
    i=i[::-1]
    l.append(i)
print(*l)