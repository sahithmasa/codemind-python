num=int(input())
s=0
while num>0:
    r=num%10
    s+=r
    num=num//10
    #print(s)
    if s>=10 and num==0:
        num=s
        s=0
print(s)