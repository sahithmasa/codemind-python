import math
n=int(input())
t=n
s=0
le=int(math.log10(n))+1
while n:
    rem=n%10
    s=s+rem**le
    n=n//10
    le-=1
if s==t:
    print("True")
else:
    print("False")