a=int(raw_input())
b=0
c=a
while a!=0:
    d=a%10
    b=b*10+d
    a=a/10
if b==c:
    print("yes")
else:
    print("no")
