
print("welcom to state bank of india!")
print("please insert your atm card...")
pin=2481
balance=500000
user_pin=int(input("enter yourfour digit pin: "))
if user_pin== pin :
    pass
    while True :
        print("""
            1 == balance
            2 == deposit balance
            3 == withdraw ba;lance
            4 == exit
            """
             )
        try:
          option=int(input("please enter your choice"))
        except:
            print("please enter valid option")
        if option==1:
             print(f"your current balance is {balance}")
        if option==2:
         withdraw_amount= int(input("enter the withdraw_amount :"))
        balance=balance-withdraw_amount
        print(f"{withdraw_amount} is debited from your account")
        print(f"your current balance is {balance}")
        if option==3:
         deposit_amount= int(input("enter the amount to be deposited :"))
        balance=balance+deposit_amount
        print(f"{deposit_amount} is credited to your account")
        print(f"your current balance is {balance}")
        if option==4:
            break
    else:
        print("you have entered the wrong pin")

