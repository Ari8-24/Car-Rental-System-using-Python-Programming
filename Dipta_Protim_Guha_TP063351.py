#Dipta Protim Guha
#TP063351



import datetime
from datetime import timedelta, date

import time
import os

#universal variables to be used throughout
programexit = 0
currentUser = "default-user"

#intro banner 
print("\n\t --- Welcome To Super Car Rental Services - SCRS --- \n")

#register function
def register():
    db = open("SCRSdatabase.txt", "r+")
    username = input(" Please eneter username: ")
    #print(username)
    userProfiles = []
    userNames = []
    for n in db:
        lines = db.readlines()
        userProfiles = [x.strip().split(', ') for x in lines] 

    for x in userProfiles:
        userNames.append(x[0])

#basic validations - check username exists or not
    if username in userNames:
        print("Username already exists")
        register()
             
    password1 = input(" Please enter password: ")
    password2 = input(" Please confirm password: ")
    usertype = input(" Register as Admin or User (A / U): ")                


#basic validations
    if password1 != password2:
        print("Passwords do not match. Please try again")
        register()
    else:
        if len(password1)<6:
            print("Password is too short. Please try again")
            register()
        else:
            db = open("SCRSdatabase.txt", "a")
            #save to textfile
            db.write(username+", "+password1+", "+usertype+"\n")
            print("Success!")
            
       

#login function
def access():
    db = open("SCRSdatabase.txt", "r")
    Username = input(" Please enter your username: ")
    Password = input(" Please enter your Password: ")

    if not len(Username or Password)<1:
        d = []
        f = []
        g = []
        for i in db:
            a,b,c = i.split(",")
            b = b.strip() #remove spaces
            c = c.strip()
            d.append(a) #add the values for username to an array/list
            f.append(b) 
            g.append(c) 
            data = dict(zip(d,f)) #dict with all username and passwords

        try:
            if data[Username]: #as long as its not empty, code can proceed
                try:
                    if Password == data[Username]:
                        print("\n *** Login Successful ***\n")
                        global currentUser
                        currentUser = Username #storing the name of the logged in user
                        
                        if evalUserType(currentUser).lower() == "a":
                            print ("Hi,", currentUser + " Admin \n")
                            adminOptions()
                            
                        elif evalUserType(currentUser).lower() == "u":
                            print ("Hi,", currentUser + " (Registered-user) \n")
                            userOptions()
                            
                        else:
                            print("Unable to find a registered user")
                        # if data[Usertype] == "U":
                        #userOptions()  
                    else:
                        print("Incorrect Username or Password")
                except:
                    print("Error Occured")
            else:
                print("Username or password does not exist")
        except:
            print("Username or password does not exist")
    else:
        print("Please enter a value")

#display the main/home menu
def homemenu(option=None):
    print("\n -- Main menu (enter an option) -- \n")   
    option = input(" 1) Login\n 2) Signup\n 3) View Cars For Rental\n 4) Exit\n\n ")
    if option == "1" or option == "l" or option == "Login" or option == "login":
        access()
    elif option == "2" or option == "s" or option == "Signup" or option == "signup":
        register()
    elif option == "3" or option == "v" or option == "View" or option == "view":
        viewCars()
    elif option == "4" or option == "e" or option == "Exit" or option == "exit":
        quit()
    else:
        print("Please enter an option")


#register a car into the system
def registerCar():
    db= open("SCRScardatabase.txt", "r+")

    today = time.strftime("%d/%m/%Y")
    print("Date today: " + today)

    plateno = input(" Enter Plate Number: ")
    carname = input(" Enter Car Brand Name: ")
    modelname = input(" Enter Car Model Name: ")
    priceperhr = input(" Cost to rent per day: ")
    rentalStatus = input(" Enter Rental Status (A / B): ")

    if rentalStatus.lower() == "a":
        rentalStatus = "A"
        dateavailable = today

    elif rentalStatus.lower() == "b":
        rentalStatus = "B"
        dateavailable = input(" Enter Date Available (e.g. format 28/06/2021): ")

        if "/" not in dateavailable:
            print("Oops, Incorrect date format.")
            registerCar()
        
    else:
        rentalStatus = "Unknown"

    d = []
    e = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        e.append(b)
    data = dict(zip(d,e))

    #basic validations
    if plateno in e:
        print("This Car Has Already Been Registered\n")
        registerCar()
    else:
        db = open("SCRScardatabase.txt", "a")
        #save to textfile
        db.write(plateno.upper()+", "+ carname + ", " + modelname + ", "+priceperhr+", "+rentalStatus+", " + dateavailable +"\n")
        print("***Car Has Been Succesfully Registered!***\n")

        adminOptions()
            
#function to check the usertype
def evalUserType(username):
    db = open("SCRSdatabase.txt", "r")
    for n in db:
        x,y,z = n.split(",")
        y = y.strip()
        z = z.strip()
        if(x == username):
            return z

#display the options available to registered users 
def userOptions():
    print("\n -- Registered User menu (enter an option) -- \n")  
    option = input(" 1) View Cars\n 2) Rent Car\n 3) View Personal Rental History\n 4) Return To Main Menu\n 5) Exit\n ")
    if option == "1":
        viewCarsAsUser()
    elif option == "2":
        rentCar()
    elif option == "3":
        viewPersonalRentalHistory()
    elif option == "4":
        homemenu()
    elif option == "5":
        quit()
    else:
        print("Please enter an option")

#display the options available to admins
def adminOptions():
    print("\n -- Admin menu (enter an option) -- \n")  
    option = input(" 1) Register Car\n 2) View cars\n 3) Modify Car \n 4) View all rental history \n 5) Return To Main Menu\n 6) Exit\n")
    if option == "1":
        registerCar()
    elif option == "2":
        viewCarsAsAdmin()
    elif option == "3":
        search_and_modify_cars()
    elif option == "4":
        viewAllRentalHistory()
    elif option == "5":
        homemenu()
    elif option == "6":
        quit()
    else:
        print("Please enter an option")
        
#function to view cars as a NON-registered user
def viewCars():
    db = open("SCRScardatabase.txt", "r")
    Lines = db.readlines()
    db.close()
    cars = []
    for index, line in enumerate(Lines):
        acar = line.strip().split(', ')
        cars.append(acar)
        #print("Line {}: {}".format(index, acar))
    
    # display car list
    print("\n -- Cars list -- \n")    

    for x in cars:
        if x[4].lower() == "a":
            print("Plate#: " + x[0] + " | Car : " + x[1] + " - " + x[2] + " | Price(per day): " + x[3] + " | Available Now")
        else:
            print("Plate#: " + x[0] + " | Car : " + x[1] + " - " + x[2] + " | Price(per day): " + x[3] + " | Booked Available From: " + x[5] )
    print("\n -- End of list -- \n")
    print("\tPlease Login/Signup to Rent a car !!! ")       


#function to view cars as a registered user 
def viewCarsAsUser():
    db = open("SCRScardatabase.txt", "r")
    Lines = db.readlines()
    db.close()
    cars = []
    for index, line in enumerate(Lines):
        acar = line.strip().split(', ')
        cars.append(acar)
        #print("Line {}: {}".format(index, acar))
    
    # display car list
    print("\n -- Cars list -- \n")    
    for x in cars:
        if x[4].lower() == "a":
            print("Plate#: " + x[0] + " | Car : " + x[1] + " - " + x[2] + " | Price(per day): " + x[3] + " | Available Now")
        else:
            print("Plate#: " + x[0] + " | Car : " + x[1] + " - " + x[2] + " | Price(per day): " + x[3] + " | Booked Available From: " + x[5])
    print("\n -- End of list -- \n")
    userOptions()

#function to view cars as a an administrator
def viewCarsAsAdmin():
    db = open("SCRScardatabase.txt", "r")
    Lines = db.readlines()
    db.close()
    cars = []
    for index, line in enumerate(Lines):
        acar = line.strip().split(', ')
        cars.append(acar)
        #print("Line {}: {}".format(index, acar))
    
    # display car list
    print("\n -- Cars list -- \n")    
    for x in cars:
        if x[4].lower() == "a":
            print("Plate#: " + x[0] + " | Car : " + x[1] + " - " + x[2] + " | Price: " + x[3] + " | Available Now")
        else:
            print("Plate#: " + x[0] + " | Car : " + x[1] + " - " + x[2] + " | Price: " + x[3] + " | Booked Available From: " + x[5])
    print("\n -- End of list -- \n")
    adminOptions()
    

def search_and_modify_cars():
    fh_r = open ("SCRScardatabase.txt","r")
    fh_w = open ("temp_modifycar.txt","w")

    plate_no = str(input("Enter the Plate number of the car: "))

    s =' '
    while(s):
        s=fh_r.readline()
        L=s.split(", ")
        if len(s)>0:
            if L[0]==plate_no:
                #plate_no=input("Enter Plate Number:")
                print("\t***Enter Update Values***\n")
                make=input("Enter the brand of the car: ")
                model=input("Enter the model of the car: ")
                price=input("Enter the price per day: ")
                rentalStatus=input("Enter A if available and B if not: ")
                today = time.strftime("%d/%m/%Y")
                if rentalStatus.lower() == "a":
                    rentalStatus = "A"
                    dateavailable = today

                elif rentalStatus.lower() == "b":
                    rentalStatus = "B"
                    dateavailable = input("Enter Date Available (e.g. format DD/MM/YYYY): ")

                    if "/" not in dateavailable:
                        print("Oops, Incorrect date format.")
                        search_and_modify_cars()
                else:
                    rentalStatus = "Unknown"


                fh_w.write(plate_no+", "+make+", "+model+", "+price+", "+rentalStatus+", "+dateavailable+"\n")
            else:
                fh_w.write(s)
        
    fh_w.close()
    fh_r.close()
    if os.path.exists("SCRScardatabase.txt"):
        os.remove("SCRScardatabase.txt")
        os.rename("temp_modifycar.txt","SCRScardatabase.txt")
    else:
        print("The file does not exist")
    
    adminOptions()


#record a new rental
def rentCar():

    db = open("SCRScardatabase.txt", "r+")
    db2 = open ("SCRSrentaldatabase.txt","a+")

    dbcars = db.readlines()
    carRecords = []
    for index, line in enumerate(dbcars):
        acar = line.strip().split(', ')
        carRecords.append(acar)

    availableCars = []
    for x in carRecords:
        if(x[4] == "A"):
            availableCars.append(x)

    if len(availableCars) ==0:
        print("\t --- Oops, No Car is available to rent. tray again later. --- \n")

    # show the cars available to rent
    if len(availableCars) >0:
        availableCarscount = len(availableCars)
        print("\n\t ---- Cars Available to rent " + str(availableCarscount) + " ----\n")
        for index, car in enumerate(availableCars):
            item = 1 + index
            print(str(item) + ") " + car[1] + " " + car[2] + " | Plate# " + car[0] + " | " + "Cost to Rent per day: " + str(car[3]) + "\n")

        print("\t --- End of list --- \n")     
    
        # Rental Form 
        cost = 0 
        print("\t !!! Rental form !!! \n")
        print("Booking person username: "  + currentUser + "\n")
        plate_no = input("Enter the Plate number of the car: ")
        plate_no = plate_no.upper()

        carfound = True
        if(len(availableCars)>0):
            for x in availableCars:
                if(x[0] == plate_no and x[4] == "A"):  
                    carfound = True
                    rent_duration = input("Enter rent duration (in days): ")
                    car = x
                    car_costperday = int(x[3])
                    total_cost = car_costperday * int(rent_duration)
                    print("To book " + car[0] + " " + car[1] + " - " + car[2] + ", it's going to cost RM " + str(total_cost) + ". \n")
                    confirm = input("Enter Y to book and pay or N to cancel booking: ")

                    if (confirm.lower() != "y"):
                        userOptions()

                    bookingdate = time.strftime("%d/%m/%Y")
                    returndate = date.today() + timedelta(days=int(rent_duration))
                    returndate = returndate.strftime("%d/%m/%Y")
                    # write to rental database
                    db2.write(plate_no+", "+currentUser+", "+str(rent_duration)+", "+"RM " + str(total_cost) + ", " + bookingdate + ", " + returndate + "\n")
                    
                    # display booking receipt
                    print("\n\t !!! Thank you for your purchase !!!" + "\n")
                    print("Booking person username: "  + currentUser + "\n")
                    
                    print("Booking Date: " + bookingdate + "\n")
                    print("Car: "+ plate_no + " " + car[1] + " " + car[2]+ "\n")
                    print("Return Date: " + returndate + "\n")
                    print("Cost per day: RM " + str(car_costperday) + "\n")
                    print("Total payable: RM " + str(total_cost)+ "\n")

                    # update car database
                    changeCarRentalStatus(plate_no,"B",returndate)
                    break
                else:
                    carfound = False

            if (carfound == False):
                print("Sorry, no car is available with Plate# " + plate_no)
    
    db.close()
    db2.close()
    
    userOptions()


#function to change car rental status
def changeCarRentalStatus(plate_no,newstatus,returndate):
    fh_r = open ("SCRScardatabase.txt","r")
    fh_w = open ("tempcardb.txt","w")

    s =' '
    while(s):
        s=fh_r.readline()
        acar=s.strip().split(", ")
        if len(s)>0:
            if acar[0]==plate_no:
                fh_w.write(acar[0]+", "+acar[1]+", "+acar[2]+", "+acar[3]+", "+newstatus+", "+returndate+"\n")
            else:
                fh_w.write(s)

    fh_w.close()
    fh_r.close()
    if os.path.exists("SCRScardatabase.txt"):
        try:
            os.unlink("SCRScardatabase.txt")
            #os.replace("tempcardb.txt","SCRScardatabase.txt")
            os.rename("tempcardb.txt","SCRScardatabase.txt")
        except OSError as e: 
            print("Failed with:", e.strerror)


    else:
        print("The file does not exist")



#function to view rental history for given user
def viewPersonalRentalHistory():
    
    rentaldb = open ("SCRSrentaldatabase.txt","r")
    print("\t Rental History of user " + currentUser + "\n")

    dbrecords = rentaldb.readlines()
    rentaldb.close()
    personalRecords = []
    for index, line in enumerate(dbrecords):
        record = line.strip().split(', ')

        if record[1] == currentUser:
            personalRecords.append(record)

    if(len(personalRecords)>0):
        for y in personalRecords:
            print("Plate#: " + y[0] + " | Total Paid : " + y[3] + " | Booking: " + y[4] + " - " + y[5] + "\n")
    
    userOptions()


#function for admin to view rental history for all or a given plate no
def viewAllRentalHistory():
    rentaldb = open ("SCRSrentaldatabase.txt","r")
    option = input(" 1) Search by a plate# \n 2) Search by customer username:\n 3) See all rental records\n")
    #to be done, not working. 
    """if option != "1" or option != "2" or option != "3": 
        print("Please enter an option")
        viewAllRentalHistory()"""
        
    plate_no = ''
    if (int(option) == 1):
        plate_no = input ("Enter the Plate#: ")
        plate_no = plate_no.upper()

    uname = ''
    if (int(option) == 2):
        uname = input ("Enter the customer username: ")
        
    dbrecords = rentaldb.readlines()
    rentaldb.close()

    allRecords = []
    filteredRecords = []
    filteredRecordsbyuser = []
    
    for index, line in enumerate(dbrecords):
        record = line.strip().split(', ')
        allRecords.append(record)
        if int(option) == 1 and record[0] == str(plate_no):
            filteredRecords.append(record)
        if int(option) == 2 and record[1] == str(uname):
            filteredRecordsbyuser.append(record)
    if (int(option) == 1):
        if(len(filteredRecords)>0):
            print("\n\t Rental History records for: " + plate_no + "\n")
            for y in filteredRecords:
                print("Plate#: " + y[0] + " | Booked By: " + y[1] + " | Total Paid : " + y[3] + " | Booking: " + y[4] + " - " + y[5] + "\n")
        else:
            print("--- No records --- ") 

    if (int(option) == 2):
        if(len(filteredRecordsbyuser)>0):
            print("\n\t Rental History records for: " + uname + "\n")
            for y in filteredRecordsbyuser:
                print("Plate#: " + y[0] + " | Booked By: " + y[1] + " | Total Paid : " + y[3] + " | Booking: " + y[4] + " - " + y[5] + "\n")
        else:
            print("--- No records --- ")          


    if (int(option) == 3):
        if(len(allRecords)>0):
            print("\n\t All Rental History records \n")
            for y in allRecords:
                print("Plate#: " + y[0] + " | Booked By: " + y[1] + " | Total Paid : " + y[3] + " | Booking: " + y[4] + " - " + y[5] + "\n")
        else:
            print("--- No records --- ")          

    adminOptions()


while(programexit!=1):
    homemenu()


