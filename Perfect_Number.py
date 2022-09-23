n=int(input())
i=1
m=0
for i in range(2,n+1,1):
    if n%i==0:
        m+=n//i
        i+=1
#print(m)
if m==n:
    print("True")
else:
    print("False")
        