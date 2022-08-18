
print("wlecome to sunitha grand")
bal=0
name= input("enter your good name")
identity= input("enter your aadhar number")
dict={'ac':1000 , 'non-ac':450} # per day
for i,j in dict.items():
    print(i,j)
room= input(" whether ac or non-ac")
if room=='ac':
    print("you have booked  a ac room")
bal+=1000 
if room=='non-ac':
    print("you have booked non-ac room")
bal+=450
print("\menu\ n1. veg \ n2. non-veg")
opt=True
while opt is True :
    opt1= int(input("choose any option (1,2)"))
if (opt1==1) :
     print("welcome to menu of veg")
     print("1. panner tikka Rs.400 \ n2. veg biryani Rs.300 \ n3. mushroom Rs.450")
     opt_1= int(input("choose any option (1,2,3"))
if (opt_1==1) :
        print("enjoy your panner tikka")
bal+=400
elif (opt_1==2) : 
        print("enjoy your veg briyani")
    bal+=300
    elif (opt_1==3) :
      print("enjoy having your mushroom curry")
bal+=450

if (opt1==2) :
   print("welcome to menu of non-veg")
print("1.chilly chicken Rs. 500 \ n2. chicken biryani Rs. 800 \ n3. kabab Rs. 350")
opt_2= int(input("choose any option (1,2,3)"))
if (opt_2==1) :
    print("enjoy is your chiily chicken ")
    bal+=500
if (opt_2==2) :
    print("enjoy your chicken biryani")
    bal+=800
if(opt_2==3) :
        print("enjoy your kabab")
        bal+=350
else:
    print("invalid option")
opt=input("sir/madam do you want to order again Yes/No ?")
from datetime import date
my_date= date(2022,5,11)
checkin= print("the date they took room",my_date)
my_date= date(2022,5,13)
checkout= print("the date tey will vacate",my_date)

    
print("your total  bill is=",bal)
print("thank you for visting")
