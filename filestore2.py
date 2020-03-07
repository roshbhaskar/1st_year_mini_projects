import json
import os

# Creating empty list everytime the program is initialized
cusnames=[]
cuspasswords=[]
cusbalance=[]
cusexist=[]

cusitem=[]
cusqty=[]
cusprice=[]
cusrate=[]

# Opening the storage files to collect the old customer data
existfile=open("Customer Database/cusexistfile.txt", "r")

namefile=open("Customer Database/cusnamefile.txt", "r")
passfile=open("Customer Database/cuspassfile.txt", "r")
balfile=open("Customer Database/cusbalfile.txt", "r")

itemfile=open("Cart Database/cusitemfile.txt", "r+")
qtyfile=open("Cart Database/cusqtyfile.txt", "r+")
pricefile=open("Cart Database/cuspricefile.txt", "r+")
ratefile=open("Cart Database/cusratefile.txt", "r+")

articlesJSON=open(os.getcwd() + '/articles.json','r').read();
articles = json.loads(articlesJSON)

# Populate the empty lists with data from the storage files

# Check list of customer names
for line in namefile:
    cusnames.append(line[:-1])
namefile.close()

# Check list of customer passwords
for line in passfile:
    cuspasswords.append(line[:-1])
passfile.close()

# Check list of customer balances
for line in balfile:
    cusbalance.append(line[:-1])
balfile.close()

# Check list for last logged in customer
for line in existfile:
    cusexist.append(line[:-1])
existfile.close()

# Check list of cart items
for line in itemfile:
    cusitem.append(line[:-1])
itemfile.close()

# Check list of cart quantity
for line in qtyfile:
    cusqty.append(line[:-1])
qtyfile.close()

# Check list of item price
for line in pricefile:
    cusprice.append(line[:-1])
pricefile.close()

# Check list of item rate
for line in ratefile:
    cusrate.append(line[:-1])
ratefile.close()
                             
# This function creates a new user
def cusaccountcheck():
    name=""
    password=""

    while name not in cusnames:
        name = raw_input("Please Type in your Name for this New Smart card.\n--> ").lower()
        if name not in cusnames:
            cusnames.append(name)
            filewrite('name',cusnames)
            cusexist = []
            cusexist.append(name)
            filewrite('exist', cusexist)
            cleancart()

        else:        
            print "Sorry, that Username is already in use..."
            ans=raw_input("Are you already a cardholder? (Y/N)\n--> ")
            if ans.lower()=='y':
                name, password, balance = oldcuscheck()
                return name, password, balance
            else:
                name=""

    while len(password)<5:
        password=raw_input("Please Assign a Password to this Account.\nPassword should be at least 5 characters\n--> ")
        print ""
                
        if len(password)>4:
            print "Your Password has been Successfully Saved."
            print "Remember to always keep your Password safe and do not Disclose it to anybody."
                        
            cuspasswords.append(password)
            cusbalance.append(0)
            balance=100.0
            cusbalance[cusnames.index(name)]=balance

            print ("\nThank you %s, Your account is set up and ready to use.\nRs. 100 has been credited to your account." %name.title())
            filewrite('pass', cuspasswords)
            filewrite('bal', cusbalance)

            break
        print "Sorry, this is a Short Password"
    return name, password, balance

# Function to check returning customer
def oldcuscheck():
    name = ""
    while name not in cusnames:
        name = raw_input("What is your name?\n--> ").lower()        
        if name in cusnames:
            username = name
            userpassword = cuspasswords[cusnames.index(name)]
            balance = float(cusbalance[cusnames.index(name)])

            if name not in cusexist:
                cusexist[:] = []
                cusexist.append(username)
                filewrite('exist', cusexist)
                cleancart()

            return username, userpassword, balance
                
        else:
            print ("Sorry %s, It looks like you didn't spell you name correctly OR Your name is not in our Records"%name.title())
            again=raw_input("Would like to type in your name again? (Y/N)\n--> ")
                        
            if again.lower()=='y':
                continue

            elif again.lower()=='n':
                print ("Bye Bye, Thank you for using Digi-Card...")
                exit()
                
            else:
                print "Wrong Choice!!! Try Again... \n\n"
                continue
        
# This function writes new data into the storage files whenever called upon.
def filewrite(filename, item):
    if filename=='name':
        text=open("Customer Database/cusnamefile.txt","w")

        for i in item:
            text.write(i+"\n")
        text.close()

    elif filename=='pass':
        text=open("Customer Database/cuspassfile.txt", "w")

        for i in item:
            text.write(i+"\n")
        text.close()

    elif filename=='bal':
        text=open("Customer Database/cusbalfile.txt", "w")

        for i in item:
            text.write(str(i)+"\n")
        text.close()

    elif filename=='exist':
        text=open("Customer Database/cusexistfile.txt", "w")
        text.seek(0)
        text.truncate()

        for i in item:
            text.write(str(i)+"\n")
        text.close()

    elif filename=='item':
        text=open("Cart Database/cusitemfile.txt", "w")

        for i in item:
            text.write(str(i)+"\n")
        text.close()

    elif filename=='quantity':
        text=open("Cart Database/cusqtyfile.txt", "w")

        for i in item:
            text.write(str(i)+"\n")
        text.close()

    elif filename=='price':
        text=open("Cart Database/cuspricefile.txt", "w")

        for i in item:
            text.write(str(i)+"\n")
        text.close()
        
    elif filename=='rate':
        text=open("Cart Database/cusratefile.txt", "w")

        for i in item:
            text.write(str(i)+"\n")
        text.close()

# This function updates the account balance after a withdraw or deposit transaction
def balupdate(ind, amount):
    accountnumber=cusnames.index(ind)
    cusbalance[accountnumber] = amount
    text=open("Customer Database/cusbalfile.txt", "w")
        
    for i in cusbalance:
        text.write(str(i)+"\n")
    text.close()

# This function deletes the selected items from the cart
def removeitem(no,q):
    I = no-1
    a = int(cusqty[I])

    if q>=a:
        del cusitem[I]
        filewrite('item',cusitem)
    
        del cusqty[I]
        filewrite('quantity',cusqty)

        del cusprice[I]
        filewrite('price',cusprice)

        del cusrate[I]
        filewrite('rate',cusrate)    
        
    else:
        i = a-q
        cusqty[I] = str(i)
        filewrite('quantity',cusqty)

        a = int(cusrate[I])*i
        cusprice[I] = str(a)
        filewrite('price',cusprice)
        
# This function adds the selected items to the cart
def additem(cArticle, cQty, cPrice, cRate):
    item = cArticle
    qty = cQty
    price = cPrice
    rate = cRate

    cusitem.append(item)
    filewrite('item',cusitem)

    cusqty.append(qty)
    filewrite('quantity',cusqty)

    cusprice.append(price)
    filewrite('price',cusprice)

    cusrate.append(rate)
    filewrite('rate',cusrate)


# This function adds te quantity of the overlapped items
def overlap(item, qty, price):
    I = item
    Q = qty
    P = price

    if I in cusitem:
        a = cusitem.index(I)
        Qu = int(cusqty[a])
        Ra = int(cusrate[a])
        Pr = int(cusprice[a])

        Quantity = Qu + Q
        Price = Ra * Quantity

        cusqty[a] = str(Quantity)
        filewrite('quantity',cusqty)
        cusprice[a] = str(Price)
        filewrite('price',cusprice)

# This function removes the items from the cart after payment
def cleancart():
    itemfile = open("Cart Database/cusitemfile.txt", "r+")
    qtyfile = open("Cart Database/cusqtyfile.txt", "r+")
    pricefile = open("Cart Database/cuspricefile.txt", "r+")
    ratefile = open("Cart Database/cusratefile.txt", "r+")

    itemfile.seek(0)
    qtyfile.seek(0)
    pricefile.seek(0)
    ratefile.seek(0)

    itemfile.truncate()    
    qtyfile.truncate()
    pricefile.truncate()
    ratefile.truncate()
    
    itemfile.close()    
    qtyfile.close()
    pricefile.close()
    ratefile.close()

# This function deletes an existing account and any data that was stored about it is cleared
def deleteaccount(name):        
    accountnumber=cusnames.index(name)
    del cusnames[accountnumber]
    filewrite('name', cusnames)

    del cusbalance[accountnumber]    
    filewrite('bal', cusbalance)
    
    del cuspasswords[accountnumber]    
    filewrite('pass', cuspasswords)

    f = open("Customer Database/cusexistfile.txt", "w").close()

    return None
