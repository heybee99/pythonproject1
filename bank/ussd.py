def landingPage():
    print("Welcome to main page")
    user = input("Enter ussd code: ").strip() 
    if user == "312":
        main()
    else:
        print("Invalid USSD code. Please input correct code") 
        landingPage()

def main():
    print(
        '''
    1. Data Plan 
    2. Buy airtime 
    3. Family data share 
    4. Social bundles 
    5. Business plan
    6. Borrow data
    7. Back
    8. Next
        ''')
    user = input("Choose your option: ")
    if user == "1":
        print("WElcome to data plan")
        data()
    elif user == "2":
         print("Welcome to airtime")
         airtime()
    elif user == "3":
        print("You can share data to your love ones")
        family()
    elif user == "4":
        print("Social bundles plan")
        social()
    elif user == "5":
        print("Business Plan here")
        business()
    elif user == "6":
        print("Borrow Data here")
        borrow()
    elif user == "7":
        print("Backii")
        landingPage()
    elif user == "8":
        print("Nextii")
        next()
    else:
         print("Invalid Option")
    
def data():
            print('''
        1. 50Mb/N200
        2. 100Mb/ 300 
        3. 200Mb/350
        4. 1Gb/ 450
            ''')
            user = input("Option?: ").strip()
            if user == "1":
                 print(f"You have purchased 50Mb of data")
            elif user == "2":
                 print("You have purchased 100Mb of data")
            elif user == "3":
                 print("You have purchased 200Mb of data")
            elif user == "4":
                 print("You have purchased 1Gb of data")
            else: 
                 print("Invalid option")
                 
def airtime():
     print('''
        1. N100
        2. N200
        3. N300 
        4. N400
        5. N500 
        ''')
     user = input("Option?: ")
     if user == "1":
          print("You have purchased N100 of airtime")
     elif user == "2":
          print("You have purchased N200 airtime")
     elif user == "3":
          print("You have purchased N300 airtime")
     elif user == "4":
          print("You have purchased N400 airtime")
     elif user == "5":
          print("You have purchased N500 airtime")
     else:
          print("Invalid option")
def family():
     print('''
        1. Share 50mb
        2. Share 100mb
        3. Share 500mb
        4. Share 1000mb
    ''')
     user = input("Option?: ")
     if user == "1":
          print("50mb successfully sahred")
     elif user == "2":
          print("100mb successfully shared")
     elif user == "3":
          print("500mb successfully shared")
     elif user == "4":
          print("1000mb successfully shared")
     else:
          print("Invalid option")
def social():
     print('''
        1. Youtube N200/1gb for 1 day
        2. Facebook N300/ 1gb for 2 days
        3. Tiktok N150/2gb for 12 hrs
        4. Instagram 300/1.5gb for 5 days
    ''') 
     user = input("Option?: ")
     if user == "1":
          print("You have purchased Youtube data bundle")
     elif user == "2":
          print("You have purchased Facebook data bundle")
     elif user == "3":
          print("You have purchased Tiktok data bundle")
     elif user == "4":
          print("You have purchased Instagram data bundle")
     else:
          print("Invalid option")
    
def business():
     print('''
        1. N500/1.2gb
        2. N600/ 1.8gb
        3. N700/ 2.3gb
        4. N1000/3.5gb
        ''')
     user = input("Option?: ")
     if user == "1":
          print("You have purchased 1.2gb business bundle")
     elif user == "2":
          print("You have purchased 1.8gb business bundle")
     elif user == "3":
          print("You have purchased 2.3gb business bundle")
     elif user == "4":
          print("You have purchased 3.5gb business bundle")
     else:
          print("Invalid option")
def borrow():
     print('''
        1. N200 to pay N250
        2. N300 to pay N350
        3. N400 to pay N450
        4. N500 to pay N550
        ''')
     user = input("Option?: ")
     if user == "1":
          print("You have borrowed N200 airtime")
     elif user == "2":
          print("You have borrowed N300 airtime")
     elif user == "3":
          print("You have borrowed N400 airtime")
     elif user == "4":
          print("You have borrowed N500 airtime")
     else:
          print("Invalid option")
def next():
     print('''
        1. Contact customer care
        2. Quit 
        3. Check balance 
        4. Check phone number
        ''')
     user = input("Options?: ")
     if user == "1":
          print("Call this number 08138744335")
     elif user == "2":
          print("You quit")
          landingPage()
     elif user == "3":
          balance = 300 
          print(f"Your balance is {balance}")
     elif user == "4":
          phoneNumber = +2348138744335 
          print(f"Your phone number is {phoneNumber}") 
     else:
          print("Invalid option")
        
landingPage() 