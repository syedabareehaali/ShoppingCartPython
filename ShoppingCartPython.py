class Stationery:
    '''Dictionary of all the items available in Shopping Cart Program.'''
    stationery=[{"id":78601,"Name":"Pencils","Available":50,"Price":20},
       {"id":78602,"Name":"Ink Pens","Available":20,"Price":30},
       {"id":78603,"Name":"Ink Removers","Available":50,"Price":50},
       {"id":78604,"Name":"Inkpots","Available":20,"Price":40},
       {"id":78605,"Name":"Glitters Set","Available":50,"Price":80},
       {"id":78606,"Name":"Pointer","Available":20,"Price":40},
       {"id":78607,"Name":"Ball Points","Available":50,"Price":20},
       {"id":78608,"Name":"Markers Set","Available":50,"Price":80},
       {"id":78609,"Name":"Highlighters","Available":20,"Price":80},
       {"id":78610,"Name":"Gel Pens","Available":20,"Price":80}]
    def Menu(self):
        pass

class Logout: 
      count=1
      def logout(self):
          '''The method ends the program.'''
          if Logout.count==1: 
            print("Logging Out........\n\nHappy Shopping!!!\n  (●*^_^*●) ")
          self.guess=False
          Logout.count=2


class Items(Stationery):
    def shopping_items(self):
        '''It prints the names and amount of available shopping items.'''
        self.Total=0
        print("\n")
        for d in self.stationery:
            print(f'{d["Name"]:12} = {d["Available"]}')
            self.Total+=(d["Available"])
        print("\nTotal available Items : ",self.Total)

          


class DisplayMenu(Stationery):
    def Menu(self):
        '''The method to display the items available in Shopping Cart Program.''' 
        print('Id\tName\t\tAvailable\tPrice')
        print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
        for d in self.stationery:
            print(f'{d["id"]}\t{d["Name"]:15}\t{d["Available"]}\t\t{d["Price"]}')


class MainLogin:
    def MainLogin(self):
        '''It prints the Main Menu.'''
        print()
        print("        **************************************")
        print("        * 1.Display Menu                     *")
        print("        * 2.Place order                      *")
        print("        * 3.Cancel order                     *")
        print("        * 4.Items Available                  *")
        print("        * 5.User's Cart                      *")
        print("        * 6.Customer Shopping Details        *")
        print("        * 7.Logout                           *")
        print("        * 8.User Personal Info (ForOwnerOnly)*")
        print("        **************************************")

        
class UserId(DisplayMenu):
    def User_id(self):
        '''The method takes int as input from User. Here Exception is handled.'''
        self.Menu()
        try:
          self.item_id=int(input("\nEnter the Item ID : "))
        except:
          print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nX ERROR ALERT!! Input Item ID in digits.X\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
          self.User_id()
   

class Order(UserId):
  MyCart=[]
  condition=True
  def Order(self):
    '''Appends the list MyCart by taking input of ID's from User. Subtracts one item from key 'Available' after MyCart is appended each time ''' 
    while Order.condition==True:
     self.User_id()
     lst=[78601,78602,78603,78604,78605,78606,78607,78608,78609,78610]
     
     if self.item_id in lst :
         
      for d in self.stationery:
          
        if d["id"]==self.item_id:
            
            print("\nId\tName\tAvailable\tPrice")
            print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            self.order='{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
            
            self.chosen=[d["id"],d["Name"],d["Price"]]
            Order.MyCart.append(self.chosen)
            
            self.check=input("\nDo you want to confirm order on this Item? [Y/N] ")

            
            if self.check=='Y' or self.check=='y':
                print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
                print("Successfully placed the order on the Item {} {}".format(d["id"],d["Name"]))
                d["Available"]-=1
                a=input('Do you Want to order more?[Y/N]\n')
                
                if a=='Y' or a=='y':
                     self.Order()        
                elif a=='N' or a=='n':
                    Order.condition=False
                    break
                else:
                    print('You have entered an invalid option')
                    a=input("\nDo you Want to order more? [Y/N] ")
                    if a=='Y' or a=='y':
                            self.Order()
                    elif a=='N' or a=='n':
                        Order.condition=False
                        break
                    else:
                        print('Ok..Back to Main Menu.')
                        Order.condition=False
                        break
                break    

                    
            elif self.check=='N' or self.check=='n' :
                print("The order is not placed. You can carry on with you purchase.")
                a=input('Want to order more?[Y/N]')

                if a=='Y' or a=='y':
                    self.Order()
                elif a=='N' or a=='n':
                    Order.condition=False
                    break
                else:
                    print('You have entered an invalid option')
                    a=input("\nWant to order more? :[ Y/N] ")
                    if a=='Y' or a=='y':
                            self.Order()
                    elif a=='N' or a=='n':
                        Order.condition=False
                        break
                    else:
                        ('Sorry, your order is not placed')
                        Order.condition=False
                        break
                break

                    
            else:
                self.check=input("\nYou have entered a wrong option.\nDo you want to check order on the Item? [ Y/N]")
                if self.check=='Y' or self.check=='y':
                    print("\nSuccessfully placed the order on the Item {} {}".format(d["id"],d["Name"]))
                    d["Available"]-=1
                    a=input('Do you want to order more?[Y/N]')
                    if a=='Y' or a=='y':
                        self.Order()
                    elif a=='N' or a=='n':
                        Order.condition=False
                        break
                    else:
                        print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
                        print('You have entered invalid alphabet')
                        a=input("\nWant to order more? :[ Y/N] ")
                        if a=='Y' or a=='y':
                            self.Order()
                        elif a=='N' or a=='n':
                            Order.condition=False
                            break
                        else:
                            ('Sorry. Your order is not placed')
                            Order.condition=False
                            break
                    break
                break
     else:
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            print('ID Not Valid\n')
            print('Input correct ID\n')
            self.Order()
    
                        

class CancelOrder(Order):
  def cancelOrder(self):
    '''Removes an item from list MyCart upon User input.'''
    if self.MyCart==[]:
        print("Sorry, your cart is empty.")
    else:    
        self.order_id=input("Enter the order id : ")
        for d in range (0,len(self.MyCart)):
              if int(self.order_id) in self.MyCart[d]:
                  self.MyCart.remove(self.MyCart[d])       
                  print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
                  print(f'{self.order_id} is removed from the placed order')
                  
                  break
          
        else: 
                  print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
                  print(f'{self.order_id} is not found')
         

        
class UserCart(Order):
    def User_Cart(self):
        '''Displays the names and details of items from list MyCart.'''
        if self.MyCart==[]:
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            print('Your cart is empty. You didn\'t purchase anything yet')
        else:
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            print('Your Cart:')
            print(f"{'ID':16}{'Item':16}{'Price'}")    
            for i in range(0,len(self.MyCart)):
                for j in range(3):
                    print(f"{str(self.MyCart[i][j]):16}",end='')
                print()

     
class UserPersonalInfo():
    def __personalInfo(self):
        '''It is a private method that displays personal info of customers to the Owner.'''
        self.ownerPassword='OwnerCS116'
        inputPassword=input("Enter Password: ")
        if inputPassword==self.ownerPassword:
            print("Here are the details of our Registered Users: ")
            for element in Login.Register:
                print(element)
                print()
        else:
            print("Incorrect Password.This info is showed to owner only.")                  

                
class UserChoice(Items,Logout,UserCart,MainLogin,CancelOrder,UserPersonalInfo):
  def UserChoice(self):
     '''It takes int as input from User and calls the respective methods.'''
     self.guess=True
     while self.guess:
        try:
          self.choice=int(input("Please enter your choice : "))
          if self.choice==1:
            print()
            self.Menu()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.MainLogin()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.UserChoice()
          elif self.choice==2:
            print()
            Order.condition=True
            self.Order()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.MainLogin()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.UserChoice()
          elif self.choice==3:
            self.cancelOrder()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.MainLogin()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.UserChoice()
          elif self.choice==4:
            self.shopping_items()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.MainLogin()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.UserChoice()
          elif self.choice==5:
            self.User_Cart()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.MainLogin()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.UserChoice()
          elif self.choice==6:
            self.displaySavedDetails()
            self.MainLogin()
            print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
            self.UserChoice()
          elif self.choice==7:
            self.logout()
          elif self.choice==8:
             print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
             self._UserPersonalInfo__personalInfo()
             print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
             self.MainLogin()
             print("\n**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n")
             self.UserChoice()
          else:
             print("\n¯\_(ツ)_/¯ \n You have selected the wrong Option.")
        except:
           print("\nXXXXXXXXXXXXXXXXXX\nX  Input digits  X\nXXXXXXXXXXXXXXXXXX\n")
           self.UserChoice()
            
             
class Login(UserChoice,UserCart):
  '''This class contains a list of registered Users. It creates User account, saves info and displays info.'''
  CurrentUser=[]
  
  print("**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**")
  print("Hey there!✿ Welcome to the Online Stationery Mart.  ")
  
  Register=[{'First Name':'Syeda Bareeha','Last Name':'Ali','Address':'Gulshan-e-Iqbal Town','Password':'123'},
            {'First Name':'Syeda Rida','Last Name':'Fatima','Address':'FB Area','Password':'abc'},
            {'First Name':'Umme','Last Name':'Hani','Address':'Gulzar-e-Hijri','Password':'100'},
            {'First Name':'Amna','Last Name':'Khan','Address':'Buffer Zone','Password':'amnapk7'},
            {'First Name':'Palwasha','Last Name':'Qasim','Address':'Gulshan','Password':'Honkong111'},
            {'First Name':'Soha','Last Name':'Abbassi','Address':'Gulistan e Johar','Password':'sa123'}]
  def login(self):
     '''It verifies the registered User from the list Register'''
     print('**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n')
     self.yn=input("HAVE USER ACCOUNT? [Y/N] : ")
     print('**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n')

     Name_check_Lst = [ i['First Name'] for i in Login.Register ]
     Last_check_Lst = [ i['Last Name'] for i in Login.Register ]
     Address_check_Lst = [ i['Address'] for i in Login.Register ]
     Pass_check_Lst=[ i['Password'] for i in Login.Register ]

     if self.yn=='Y' or self.yn=='y' :
        self.FirstName=input("Enter your First Name: ")
        for i in range(0,len( Name_check_Lst)):
          if self.FirstName== Name_check_Lst[i]:
            self.password=input("Please Enter Your Password : ")

            if self.password== Pass_check_Lst[i]:
                print("Dear Customer,you have Successfully Logged in!\n\n")
                Login.CurrentUser.extend([Name_check_Lst[i],Last_check_Lst[i],Address_check_Lst[i]])
                self.MainLogin()
                self.UserChoice()

            else:
                print("Incorrect Password !! Please input Again: ")
                self.password=input()
                if self.password == Pass_check_Lst[i]:
                    print("Dear Customer,you have Successfully Logged in!\n\n")
                    Login.CurrentUser.extend([Name_check_Lst[i],Last_check_Lst[i],Address_check_Lst[i]])
                
                    self.MainLogin()
                    self.UserChoice()
                else:
                    print("Password is not valid")
                    break            
                
     elif self.yn=='N' or self.yn=='n' :
         Register_User={}
         self.FirstName=input("Enter First Name: ")
         self.LastName=input("Enter Last Name: ")
         self.Address=input("Enter Address: ")
         self.password=input("Enter a strong Password: ")
         Register_User['First Name']=self.FirstName
         Register_User['Last Name']=self.LastName
         Register_User['Address']=self.Address
         Register_User['Password']=self.password
         Login.Register.append(Register_User)
         Login.CurrentUser.extend([self.FirstName,self.LastName,self.Address])
         
    
         self.MainLogin()
         self.UserChoice()    
     
                
     else:
         print("Please Input the correct option\n")
         self.login()

     self.save() 

  def get_record(self):
         '''Getter Method for Users' record.'''
         self.MyCartItem=[]
         self.record=self.CurrentUser+self.MyCart


  def save(self):
         '''Method for saving User Records in file.'''
         self.get_record()
         f=open('C:\\Users\\DELL\\Documents\\UserRecords4thFile.txt','a')
         for i in range(0,len(self.record)):
             f.write(f"{str(self.record[i]):22}")
         f.write('\n') 
         f.close()


  def displaySavedDetails(self):
      '''The method displays the relevant shopping details to User from file.'''
      self.save()
      print('\n\n                                        $$$$$~~~~~~~~~~CUSTOMERS DETAILS~~~~~~~~~~~~~$$$$$                    ')
      print('**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**')
      print(f"{'First Name':22}{'Last Name':22}{'Address':28}{'UserCart'}\n")
      print('**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**')
      f=open('C:\\Users\\DELL\\Documents\\UserRecords4thFile.txt','r')
      for line in f:
          print(line)
          print()
      print('**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**\n')
      f.close()

 

           
a=Login()
a.login()












