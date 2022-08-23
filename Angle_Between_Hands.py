HHMM=input()
a=int(HHMM[0:2])
b=int(HHMM[3:])
c=a*30
d=(11/2)*b
e=abs(c-d)
q=abs(360-e)
if e<q:
    print(e)
else:
    print(q)
    