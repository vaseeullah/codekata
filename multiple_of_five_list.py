n=int(input())
lis=[]
for i in range(n):
    lis.append(int(input()))
for i in range(0,len(lis)):
    if lis[i]%5==0:
        print(lis[i])

