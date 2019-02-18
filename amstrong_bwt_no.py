a,b=raw_input().split()
a=int(a)
b=int(b)
for i in range(a,b):
    d=len(str(i))
    sum=0
    c=i
    while c>0:
        e=c%10
        sum+=e**d
        c//=10
    if i==sum:
        print(i),
