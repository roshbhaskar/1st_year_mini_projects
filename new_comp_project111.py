intro="Welcome to Indian Railway Registrations"
print(intro.center(50,'*'))
print("INSTRUCTIONS:")
print("1.While creating an account ensure the following:\n i)Username must  have atmost 15 characters and should include an '_' and can include alphabets and numbers")
print("ii)Do not include spaces while entering the first name and it should be atmost 15 characters")
print("iii)Password should be only alphanumerical and must be at least 7,and at most 15 characters long.")
print("2.If already existing user,ensure that username and password are entered properly.")
print("Happy Booking".center(30,'#'))
print("*********\n")
print("WELCOME TO INDIAN RAILWAY RESERVATIONS")
D={}
D1={}
print(' ')
L_name=[]
L_ph=[]
L_lastname=[]

while True:
    x=input('Are you an existing user?(y/n) :')
    if x=='n':
        
                
              
                    
                    print("Please enter the following details :",end='\n')
                    while(True):
                        user_name=input("Username :")
                        if(('_'  in user_name)&(len(user_name)<15)):
                               file1=open('username.txt','a')
                               file1.write(user_name+'\n') #appending the usernames into the file. Backslash is used so that new usernames are added to new lines
                               file1.close()
                               break
                        else:
                               print("Please enter Valid username and do include underscore!")
                    while(True):
                        f_name=input("First Name :")
                        if((' '  not in user_name)&(len(user_name)<15)&(f_name.isalpha()==True)):
                               file2=open('name.txt','a')
                               file2.write(f_name +'\n')
                               file2.close()
                               L_name.append(f_name)
                               break
                        else:
                               print("Please enter Valid first name!")
                    while(True):
                        l_name=input("Last Name :")
                        if(l_name.isalpha()==True):
                                L_lastname.append(l_name)
                                break
                        else:
                               print("Please enter Valid last name!")  
                    while(True):
                        ph_no=input("Mobile Number :")
                        if((ph_no.isdigit()==True)&(len(ph_no)==10)):
                               L_ph.append(ph_no)
                               break
                        else:
                               print("Please enter Valid phone number!")
                    while(True):
                        e_mail=input("Email id :")  
                        if(('@'  in e_mail)&(len(e_mail)<20)&('.' in e_mail)):
                               break
                        else:
                               print("Please enter Valid email id!")
                    while(True):
                        password=input("Password :") #should do password validation
                        if((len(password)>7) &(len(password)<15)& password.isalnum()==True):
                               print('Please proceed for booking ')
                               print(' ')
                               file3=open('password.txt','a')
                               file3.write(password+'\n')
                               file3.close()
                               break
                        else:
                               print("Password not strong enough Please enter again with numbers!")
                       
                    
                            
                    break
                   
        
                        
                    
    if x=='y':
        filea=open('username.txt','r')
        fileb=open('password.txt','r')
        a=filea.readlines()
        b=fileb.readlines()
        d=dict(zip(a,b))
        #print(d)#these dict will be printed for your reference time being we will remove these while submiting it lol
        filea.close()
        fileb.close()
        filea=open('username.txt','r')
        filec=open('name.txt','r')
        e=filea.readlines()
        f=filec.readlines()
        d1=dict(zip(e,f))
        #print(d1)# these are just to show you how the data is stored inside the dict
        filea.close()
        filec.close()
            
        while True:
                
                    u_name=input('Enter your username :')
                    if u_name+'\n' in d: #checking if username really exists
                        L_name.append(d1[u_name+'\n']) #appending the name to an empty list for temporary storage, to be called later on
                        pas_word=input('Enter password :')
                        
                        if d[u_name+'\n']!=(pas_word+'\n'):#checking validation
                            print('Wrong password, Try again!')
                            continue
                        else:
                            print('*******')
                            print(' ')
                            print('Welcome',d1[u_name+'\n'])#calling your name
                            print('Please proceed for booking')
                        break
                       
                    else:
                            print('Invalid Username')
                            continue
        break

    else:
        print('invalid input')
        continue



                    
               
    

import time,math,random

def BOOKING(L_name,L_ph,L_lastname):
    print("Train number         Train Name ")
    print("CE1092               Chennai Express\nSH2891               Shatabdhi\nBE1256               Bangalore Express\nAE7883               Andra Express\nRD5002               Rajdhani\nTE3921               TamilNadu Express")
    dd1={"CE1092":"Chennai Express","SH2891":"Shatabdhi","BE1256":"Bangalore Express"}
    dd11={"AE7883":"Andra Express","RD5002":"Rajdhani","TE3921":"TamilNadu Express"}
    DD1={}
    for i in (dd1,dd11):
        DD1.update(i)#updating the contents of dict dd1 and dd11 into DD1
    dd2={"CE1092":5,"SH2891":1,"BE1256":4,"AE7883":2,"RD5002":3,"TE3921":4}
    dd3={"CE1092":"10:30    12:45    20:00","SH2891":"7:00    21:30","BE1256":"6:00    18:00    24:00","AE7883":"5:00    12:00    22:00","RD5002":"8:00    15:00","TE3921":"9:00    16:00"}
    print("Enter details of your travel:")
    L_month=[]
    L_date=[]
    L_time=[]
    def booking():
        while True:
            print(" ")
            month=int(input("enter the month of travel(mm) :"))
            
            if month>0 and month<13:#checking month validity 
                    L_month.append(month)
                
                    date=int(input("enter the date of travel(dd) :"))
                    L_date.append(date)#appending the date into a empty list 
                
                    if date>0 and date<32:
                        
                            print("These are the available trains :")
                            print(' ')
                            if int(date)%2==0:
                                for i in dd1:
                                    print(dd1[i])#used for printing one set of trains
                                    print(' ')
                                sat=input("unsatisfied with the available trains?\nwould you like to try some other date?(y/n) :")
                                if sat=="y":
                                    print(".....")
                                    continue
                                else:
                                    print(".....")
                                    break
                            else:
                                for i in dd11:
                                    print(dd11[i])#used for printing another set of trains
                                    print(' ')
                                sat=input("unsatisfied with the available trains?\nwould you like to try some other date?(y/n) :")
                                if sat=="y":
                                    print(".....")
                                    continue
                                else:
                                    print(".....")
                                    break
                    else:
                            print("invalid date try again")
                            
                    

            else:
                print("invalid month try again")
                continue
        
    booking()


    def payment():           
        while True:
            print(" ")
            no=input("Please choose the desired train\nand enter its correct train number from the table above :")
            train_no=no.upper()
            
            if train_no in dd2:
                seats=int(input("Select the number of seats :"))
                if seats<=dd2[train_no]:
                    dd2[train_no]=dd2[train_no]-seats# checking the availability of the number of seats
                    break
                else:
                    print("Sorry! these seats arent available try a different train :")
                    continue
            else:
                print("Invalid train number! Please try again.")
                continue

        while True:
                print(' ')
                print("These are the available time slots for your train :")
                print(dd3[train_no])#shows the time slots
                x=input("Satisfied with the time slots?\nWanna change the date or month?(y/n) :")
                if x=='n':
                    time_slot=input("enter the seclected time slot(hr:min) :")
                    L_time.append(time_slot)
                    print("Proceeding for payment please wait :")
                    print(".")
                    time.sleep(0.5)#this function pauses the program for the mentioned number of seconds
                    print("."),time.sleep(1),print(".")
                    break
                else:
                    booking()

        while True:
                print(" ")
                card=input("Enter your 10 digit card number :")
                if card.isnumeric() and len(card)==10:#validation of card number
                    print("Your booking was suceesful ")
                    break
                    
                else:
                    print("Invalid info, try again")
                    continue
        while True:
            ticket=input("Would you like to have a mini ticket?(y/n) :")
            print('******')
            if ticket=='y':
                print(' ')
                print('Name :',L_name[0])
                print('Train number :',train_no,"            ","Train Name :",DD1[train_no],'           ','Time :',L_time[0])
                print('Date :',L_date[0],'            ','Month :',L_month[0],'           ','Year :','2018')
                print('Ticket number :',random.randint(1,100000000000))#this function generates a random ticket number for the user
                print(' ')
                print("Thank You for using our site")
                print("HAVE A SAFE JOURNEY!")
                print(' ')
                print("********")
                break
            else:
                print("Thank You for using our site")
                print("HAVE A SAFE JOURNEY!")
                print(' ')
                print("********")
                break
                



    payment()
BOOKING(L_name,L_ph,L_lastname)
    


    
    



















        
