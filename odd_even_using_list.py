n=int(input())
lis=[]
for i in range(n):
    lis.append(int(input()))
odd=[]
even=[]
for i in range(0,len(lis)):
    if lis[i]%2==0:
        even.append(lis[i])
    else:
        odd.append(lis[i])
print("odd list",odd)
print("even list",even)
