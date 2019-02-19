print("************WELCOME TO VAP TRAVELS**********")
slocation=("Central")
dlocation=["OMR","ECR","Avadi"]
tdist=[35,30,25]
cart=["nano","micro","mini","prime"]
stat=["confirmed","not confirmed"]
nano=5
micro=7
mini=8
prime=10
print("please select your destination\n1.OMR 2.ECR 3.Avadi")
pchoice=int(input())
print(dlocation[pchoice-1],"is your destination")
if pchoice==1:
    a=tdist[0]
elif pchoice==2:
    a=tdist[1]
else:
    a=tdist[2]
print("distance of the destination is:",a,"KM")
print("********************************************")
print("please select your car type\n1.nano 2.micro 3.mini 4.prime")
cchoice=int(input())
print(cart[cchoice-1],"is your selected car type")
if cchoice==1:
    b=a*nano
elif cchoice==2:
    b=a*micro
elif cchoice==3:
    b=a*mini
else:
    b=a*prime
print("amount for your travel is:",b,"Rupees")
print("**********************************************")
print("do you confirm your travel\n1.yes 2.no")
bchoice=int(input())
if bchoice==1:
    print("your booking is",stat[bchoice-1] )
else:
    print("your booking was",stat[bchoice-1],", please confim again")
print("************************************************")
print("your desination is",dlocation[pchoice-1])
print("total distance is",a,"KM")
print("selected car type is",cart[cchoice-1])
print("amount for your travel is",b)
print("current status:",stat[bchoice-1])
