n=input()
n=int(n)
lis=[]
for i in range(n):
    lis.append(input())
v=['a','e','i','o','u']
vowel=[]
consonant=[]
for i in range(0,len(lis)):
    if lis[i].isalpha():
        if lis[i] in v:
            vowel.append(lis[i])
        else:
            consonant.append(lis[i])
print(vowel)        
print(consonant)
