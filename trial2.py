import filestore2
import time, datetime, pickle
articleBase = filestore2.articles

# This is the function that is called at the beginning of the program - Main_Page                                                                      
def postcard():                                                                     
    print ("Welcome to Digi-World, Hustle and Heart set us apart.\n")               
                                                                                        
    prompt=raw_input("""To apply for a new store card, Press 1.\n"""+                                    
                        """To access your existing account, Press 2.\n--> """)      
                                                                                        
    if prompt == '1':                                                               
        cus=CardAccount()                                                           
        # Creates a new customer profile                                            
                                                                                    
    elif prompt == '2':                                                             
        cus=ReturnCustomer()                                                        
        # Checks for existing customer                                              
                                                                                    
    else:                                                                           
        print ("You have Pressed the Wrong Key, Please try again.\n\n")
        postcard()                                                                  
                                                                                    
# Class for creating an instance of a new back account and other default bank functions
class CardAccount:
    # Class for a Card Account
    type="Normal Account"

    def __init__(self):
        # Calls functions in the module filestore2
        self.username, self.userpassword, self.balance=filestore2.cusaccountcheck()
        self.userfunctions()

    # This function shows the choices to the user - Main_Page
    def userfunctions(self):
        print("\n\nTo access any function below, Enter the corresponding key:")
        print ("""To
Check Balance,  Press B.
Deposit Cash,   Press D.
Withdraw Cash,  Press W
Buy Products,   Press P.
View Cart,      Press V.
Delete Account, Press X.
Exit Service,   Press E.
-->"""),
        ans=raw_input("").lower()

        if ans == 'b':
            self.checkbalance()

        elif ans == 'd':
            # This function confirms stored password with user input
            self.passcheck() 
            self.depositcash()
            
        elif ans == 'w':
            self.passcheck()
            self.withdrawcash()

        elif ans == 'p':
            self.passcheck()
            self.buyproducts()

        elif ans == 'v':
            self.viewcart()

        elif ans == 'x':
            self.passcheck()
            print ("%s, Your Account is being Deleted..."%self.username.title())
            print ("")            
            time.sleep(2)
            filestore2.deleteaccount(self.username)
            print ("Your Account has been Successfully Deleted.\nThank You for using Digi-World Services.")

        elif ans == 'e':
            print ("Thank you for using Digi-World Services.")
            time.sleep(1)
            print ("Goodbye... %s" %self.username.title())
            exit()

        else:
            print ("No Function assigned to this key, Please try again.")
            self.userfunctions()

    # This function returns the current balance of the account holder - Functions
    def checkbalance(self):
        date=datetime.date.today()
        date=date.strftime('%d-%B-%Y')
        
        self.working()
        print ("\nYour Account Balance as on {} is {}").format(date, self.balance)
        self.transact_again()
        

    #This function shows the choice of products for buying - Products2
    def buyproducts(self):
        #Pick department
        while True:
            print("Choose a Department: ")
            departments = articleBase['departments']
        
            for departmentID in range(len(departments)):
                print ("{}. {}.".format(str(departmentID+1),departments[departmentID]['name'])
            cho = raw_input("\nPick a Department between 1 and " + str(len(departments)) + ".\n--> ")

            if cho.isdigit() == True:
                choice = int(cho)
                if choice <= len(departments) and choice > 0:
                   chosenDepartment = departments[choice-1]
                   break
            print "Wrong Choice !!! Try Again...\n"
        
        #Pick category
        while True:
            print ""
            print("Choose a Category: ")
            categories = chosenDepartment['categories']
        
            for categoryID in range(len(categories)):
                print "{}. {}.".format(str(categoryID+1),categories[categoryID]['name'])
            cho = raw_input("\nPick a Category between 1 and " + str(len(categories)) + ".\n--> ")

            if cho.isdigit() == True:
                choice = int(cho)
                if choice <= len(categories) and choice > 0:
                    chosenCategory = categories[choice-1]
                    break            
            print "Wrong Choice !!! Try Again...\n"

        #Pick article
        while True:
            print ""
            print("Choose an Article: ")
            articles = chosenCategory['articles']        
            for articleID in range(len(articles)):
                print "{}. {}....... Rs. {}".format(str(articleID+1),articles[articleID]['name'],articles[articleID]['price'])
            cho = raw_input("\nPick an Article between 1 and " + str(len(articles)) + ".\n--> ")
            Qty = raw_input("Enter Quantity Required. \n--> ")
            
            if cho.isdigit() == True:
                choice = int(cho)
                if choice <= len(articles) and choice > 0:
                    chosenArticle = articles[choice-1]
                    if Qty.isdigit() == True and int(Qty) > 0:
                        cQty = int(Qty)
                        break
            print "Wrong Choice !!! Try Again...\n"

        cArticle = articles[choice-1]['name']
        cRate = articles[choice-1]['price']
        cPrice = cRate * cQty
        
        a = self.checkoverlap(cArticle)
        if a == True:
            filestore2.overlap(cArticle, cQty, cPrice)
        elif a == False:
            filestore2.additem(cArticle, cQty, cPrice, cRate)        
        time.sleep(0.50)
        print("The Item's Price is Rs. " + str(cQty*chosenArticle['price']))        
        self.working()
        self.transact_again()

    # This function checks for any overlapping items 
    def checkoverlap(self, item):
        I = ""
        I = "{}\n".format(str(item))
        Item = []

        with open("Cart Database/cusitemfile.txt") as sourcefile1:
            Item = sourcefile1.readlines()

        try :
            if I in Item:
                return True
            else:
                return False
                
        except ValueError:
            pass
        
    # This function shows the selected items
    def viewcart(self):
        cartitem=open("Cart Database/cusitemfile.txt", "r")
        cartqty=open("Cart Database/cusqtyfile.txt", "r")
        cartprice=open("Cart Database/cuspricefile.txt", "r")
        cartrate=open("Cart Database/cusratefile.txt", "r")

        with cartitem as i:
            items = [line.strip() for line in i]            
        with cartqty as i:
            qtys = [line.strip() for line in i]            
        with cartprice as i:
            prices = [line.strip() for line in i]
        with cartrate as i:
            rates = [line.strip() for line in i]
        
        for ID in range(len(items)):
            print "{}. {}............... Rs. {}".format(str(ID+1),str(items[ID]),str(rates[ID]))
            print "   x",qtys[ID],"         --> Rs.",prices[ID],"\n"

        cartitem.close()
        cartqty.close()
        cartprice.close()
        cartrate.close()
            
        time.sleep(1.5)
        self.paycart()
                
    # This function pays for the item in the cart, reducing your balance - View      
    def paycart(self):
        cart = open("Cart Database/cuspricefile.txt", "r")
        sub = cart.readlines()
        total = 0

        for i in sub:
            printnum=0
        
            try:
                printnum += float(i)
                total += printnum
            
            except ValueError:
                print "Invalid Literal for int() with Base 10: ",ValueError
                
        print "The Total Amount to be Paid is Rs.",total,"\n"
        if total!=0:
            choice = raw_input("Do You want to Remove any items from the Cart? (Y/N)\n--> ").lower()
            if choice == 'y':
                it = raw_input("Enter the Item number to be Removed \n--> ")
                qy = raw_input("Enter the No. of Items to be Removed \n--> ")
                if it.isdigit() == True and qy.isdigit() == True:
                    # Confirming qty for numbers
                    removeit = int(it)
                    removeqty = int(qy)
                    while True:
                        Quant = open("Cart Database/cusqtyfile.txt", "r")
                        l = []
                        l = Quant.readlines()
                        Quant.close()
                        if len(l) > (removeit-1) and (removeit) > 0:
                            # Confirming qty for range
                            filestore2.removeitem(removeit,removeqty)
                            break
                        else:
                            print "Wrong Choice!!! Try Again...\n\n"
                            self.viewcart()
                            
                    self.viewcart()    
                else:
                    print "Wrong Choice !!! Try Again...\n\n"
                    self.viewcart()  
                    
            elif choice == 'n':
                pay = raw_input("Do You want to Pay for the Items in the Cart now? (Y/N)\n--> ").lower()

                if pay == 'y':
                    self.working()
                    if self.balance >= total:
                        self.balance -= total

                        print ("\nYour new Account Balance is Rs. %.2f" %self.balance)
                        filestore2.cleancart() 
                        filestore2.balupdate(self.username, self.balance)

                    else:
                        print "Insufficient Funds !!!"
                        print "Deposit Cash and Try Again later..."
                        
                elif pay == 'n':
                    print "\nItems Remain in the Cart Till you Check-out..."
                    time.sleep(1)
                    
                else:
                    print "Wrong Choice !!! Try Again...\n\n"
                    self.viewcart()
            else:
                print "Wrong Choice !!! Try Again...\n\n"
                self.paycart()


        elif total==0:
            print "Your Cart is Empty..."
            choose = raw_input("Do You want to Buy Products, now? (Y/N)\n--> ").lower()
            if choose == 'y':
                self.passcheck()
                self.buyproducts()
            else:
                print "Leading to Home Page..."
                self.working()
                self.userfunctions()
        
        self.transact_again()

    # This function increases your balance - Functions       
    def depositcash(self):
        am=raw_input("Please Enter Amount to be Deposited to Card. \n--> ")
        if am.isdigit()==True:
            amount = int(am)
            self.balance += amount
            self.working()
        
            print ("\nYour new Account Balance is Rs. %.2f" %self.balance)     
            filestore2.balupdate(self.username, self.balance)
            self.transact_again()
        else:
            print "Wrong Choice !!! Try Again...\n"
            self.depositcash()
            
    # This function decreases your balance - Functions       
    def withdrawcash(self):
        am=raw_input("Please Enter Amount to be Withdrawn from Card. \n--> ")
        if am.isdigit()==True:
            amount = int(am)
            self.balance -= amount
            self.working()
        
            print ("\nYour new Account Balance is Rs. %.2f" %self.balance)     
            filestore2.balupdate(self.username, self.balance)
            self.transact_again()
        else:
            print "Wrong Choice !!! Try Again...\n"
            self.withdrawcash()

    # This function lets the user transact again - Functions
    def transact_again(self):
        print ""
        ans=raw_input("Do You want to do any other Transaction? (Y/N)\n--> ").lower()

        if ans=='y':
            self.working()
            self.userfunctions()
            
        elif ans=='n':
            print ("\nThank you for using Digi-card... Have a Good Day.")
            time.sleep(1)
            print ("Goodbye, {}.").format(self.username.title())
            exit()
            
        elif ans!='y' and ans!='n':
            print "Unknown key pressed, Please choose either 'N' or 'Y'\n"
            self.transact_again()


    def working(self):        
        print("working"),
        time.sleep(0.75)
        
        print ("..."),
        time.sleep(0.75)
        
        print("..."),
        time.sleep(0.75)
        
        print ("..."),
        time.sleep(0.75)
        
        print("..."),
        time.sleep(1)
        
    # This function confirms stored password with user input
    def passcheck(self):
        # Prompts user for password for each function and counterchecks it with stored passwords.
        b=3
        while b>0:
            print "Passwords are Case Sensitive..."
            ans = raw_input("Please Type in your Password to Continue with the function.\n--> ")
            if ans == self.userpassword:
                return True

            else:
                print "That is the Wrong Password."
                b-=1
                print ("%d more Attempt(s) Remaining.\n" %b)

        print ("Smart Card Account has been freezed due to 3 wrong Password attempts.\nContact our Reception for help.")
        
        time.sleep(1)
        print ("..."),
        
        time.sleep(1)
        print("...")
        
        time.sleep(1)
        exit()

class ReturnCustomer(CardAccount):
    type="Normal Account"
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore2.oldcuscheck()
        self.userfunctions()

postcard() # calling the function to run the program
