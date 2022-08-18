



class mobile :
    def __init__(self,name,company,ram,internalstorage,price):
        self.a= name
        self.b= company
        self.c= ram
        self.d= internalstorage
        self.e= price 
    def mobile_info(self):
        print("mobile name: ",self.a)
        print("company of the mobile: ",self.b)
        print("ram: ",self.c)
        print("internal storage: ",self.d)
        print("price: ",self.e)
mobilename=input("Enter the mobile name: ")
mobilecompany=input("Enter the company name: ")
mobileram=int(input("enter the mobile ram: "))
mobilestorage=int(input("Enter the internal storage: "))
mobileprice=int(input("enter the price of the mobile: "))
mobileobj= mobile(mobilename,mobilecompany,mobileram,mobilestorage,mobileprice)
mobileobj.mobile_info()
