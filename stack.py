print("welcome to stack")
ser=["insert a value fom the list","remove value from the list","find the length of the list","check it is empty or not","exit"]
exit=["yes","no"]
a=[]
while True:
    print("which one of our service did you want?\n1.insert a value fom the list \n2.remove value from the list \n3.find the length of the list\n4.check is is empty or not \n5.exit")
    customerchoice=int(input())
    if customerchoice==1:
        print("you are select to",ser[customerchoice-1])
        print("please enter the value")
        invalue=input()
        a.append(invalue)
        print("now your list is:",a)
    elif customerchoice==2:
        print("you are select to",ser[customerchoice-1])  
        if len(a)==0:
            print("it is a empty list")
        else:    
            a.pop()#for queue a.pop(0)
            print("now your list is",a)
    elif customerchoice==3:
        print("you are select to",ser[customerchoice-1])  
        print("now your list has",len(a),"values")
    elif customerchoice==4:
        print("you are select to",ser[customerchoice-1])  
        if len(a)==0:
            print("your list is empty")
        else:
            print("your list is not empty and your list is:",a)
    else:
        print("are you confirm to",ser[customerchoice-1])
        print("thank you,visit again")
        break
