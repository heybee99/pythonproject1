import mysql.connector as sq 
import datetime as dt 
import time 
import random 
import pwinput as pw 
import regex as rg

myconnect = sq.connect( 
        host="127.0.0.1",
        user="root",
        password="",
        database="bankApp" 
)
mycursor = myconnect.cursor() 
myconnect.autocommit = True  
# mycursor.execute("CREATE DATABASE bankApp") 
# mycursor.execute("CREATE TABLE customer_table (ID INT(10) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(40), email VARCHAR(50) UNIQUE, password INT(100), transaction_pin INT(4), phone_no VARCHAR(11) UNIQUE, account_type VARCHAR(60), address VARCHAR(20), kin VARCHAR(20), account_no VARCHAR(10) UNIQUE, account_balance FLOAT(30), date_created DATETIME DEFAULT CURRENT_TIMESTAMP)") 
# mycursor.execute("CREATE TABLE staff_table (ID INT(10) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(40), email VARCHAR(50) UNIQUE, password INT(100), phone_no VARCHAR(11) UNIQUE, address VARCHAR(20), department VARCHAR(50), date_created DATETIME DEFAULT CURRENT_TIMESTAMP)") 
# mycursor.execute("CREATE TABLE transaction_tables (transaction_id INT(10) PRIMARY KEY AUTO_INCREMENT, account_no VARCHAR(10), amount FLOAT(50), transaction_type VARCHAR(50), sender_account VARCHAR(11), reciever_account VARCHAR(11), reference VARCHAR(50), transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP)") 
  

class Mybank: 
    def __init__(self):
        self.name = "HEYBEE Bank" 
        self.account_No = str(random.randint(3030000000, 3039999999)) 
        self.account_balance = float(0) 
        self.time = dt.datetime.now().ctime()   
        self.branch = "Lagos" 
        self.mycursor = myconnect.cursor()
        print(self.time)
        self.landingPage() 

    def landingPage(self): 

        print(f"********************** Welcome to {self.name} **********************")
        time.sleep(1) 

        print("""
        1. Create Account 
        2. Login
        3. Forget password? 
        
        """) 

        user = input("Input option: ") 
        if user.strip() == "1":
            print("""
            1. Create as Staff
            2. Create as Customer 
            3. back 
            """)
            user2 = input("Input Option: ").strip() 
            if user2 == "1":
                self.staff() 
            elif user2 =="2": 
                self.create() 
            elif user2 =="3":
                self.landingPage() 
            else:
                print("Invalid Option")
        elif user == "2":
            print("""
            1. Login as Staff
            2. Login as Customer
            3. back 
            """)
            user3 = input("Input Option: ").strip() 
            if user3 == "1":
                self.staff_login()
            elif user3 =="2":
                self.login() 
            elif user3 == "3":
                self.landingPage()
            else:
                print("Invalid Option") 
        elif user == "3":
            self.forget_password()
        else:
            print("invalid input")
            time.sleep(2)
            self.landingPage()
    def staff(self):
        print("Welcome to staff page") 
        fullname = input("Full Name: ")
        email =input("Enter your email: ")
        password = self.inputPassword()
        phone_no = input("Enter your Phone Number: ")
        address = input("Enter your Address: ") 
        department = input("Enter your department: ")

        try: 
            query = "INSERT INTO staff_table(fullname, email, password, phone_no, address, department) VALUES ( %s, %s, %s, %s, %s, %s)" 
            value = (fullname, email, password, phone_no, address, department)
            self.mycursor.execute(query, value) 
            
        except Exception as e:
            print(f"Something went wrong {e}")  
        except:
            print("Email already exist, enter another email")
            self.staff()
        else:
            print(f'''
            Congratulations {fullname} your account has been created successfully. 
            We welcome you to our team
            
            Kindly Login to your account ----> 

            ''')     
            self.staff_login()
    def staff_login(self): 
        self.staff_email = input("Enter your email: ")
        self.staff_password = input("Enter your password: ") 

        query2 = "SELECT fullname, email, password, department FROM staff_table WHERE email = %s AND password = %s"
        value2 = (self.staff_email, self.staff_password ) 
        self.mycursor.execute(query2, value2) 
        details = self.mycursor.fetchall()
        try:
            self.staff_name = details[0][0]
            self.staff_email = details[0][1]
            self.staff_password = details[0][2] 
            self.department = details[0][3]
            
        except:
            print("Wrong email or password ")
            user = input("Press ENTER to retry or 1 to go back to menu: ")
            while user != "1":
                self.login()
            self.landingPage() 
        else:
            print(f'''  Welcome back {self.staff_name})
                        Let's get started ''')  
            self.staffdashboard() 
    def staffdashboard(self):
        print("""
            1. View all registered customers details 
            2. Check customer transaction history 
            3. View personal profile 
            4. View customer details by account no
            5. Delete customer account / transaction  
            6. log out 
            """)
        staff_option = input("Options: ")
        if staff_option == "1":
            self.reg_customer()
        elif staff_option == "2":
            self.customer_tranc()
        elif staff_option == "3":
            self.staff_profile()
        elif staff_option == "4":
            self.reg_detail() 
        elif staff_option == "5":
            self.delete()
        elif staff_option == "6":
            self.landingPage() 
        else:
            print("Invalid") 
    
    def delete(self):
        print("Delete customer account/ transaction ")
        option = input("1 to delete account and 2 to delete transaction")
        if option == "1": 
            self.delete_acc() 
        elif option == "2":
            self.delete_tran() 
        else:
            print("Invalid choice") 
    def delete_tran(self):
        try:
            self.account_no = int(input("Enter customer account number: ").strip()) 
        except ValueError: 
            print("Invalid account") 
        else: 
            confirm = input("Are you sure you want to delete? press ENTER to delete and 1 to terminate:  ") 
            if confirm == "1": 
                self.staffdashboard()
            else: 
                query = "DELETE FROM transaction_tables WHERE account_no = %s " 
                value = (self.account_no, )  
                self.mycursor.execute(query, value) 
                time.sleep(1)
                print(f"Transaction details of {self.account_no} has been deleted!")
                time.sleep(1) 
            opt = input("Press ENTER to continue and 1 to back: ") 
            if opt != "1": 
                self.delete() 
            else:
                self.staffdashboard() 
    def delete_acc(self):    
        try:
            self.account_no = int(input("Enter customer account number: ").strip()) 
        except ValueError:
            print("Invalid account") 
        else: 
            confirm = input("Are you sure you want to delete? press ENTER to delete and 1 to terminate:  ") 
            if confirm == "1": 
                self.staffdashboard() 
            else: 
                query = "DELETE FROM customer_table WHERE account_no = %s " 
                value = (self.account_no, )  
                self.mycursor.execute(query, value) 
                time.sleep(1)
                print(f"Notification: >>> {self.account_no} has been deleted!") 
                time.sleep(1)
            opt = input("Press ENTER to continue and 1 to back: ") 
            if opt != "1": 
                self.delete() 
            else:
                self.staffdashboard()  

    def reg_customer(self): 
        try:   
            query2 = "SELECT * FROM customer_table  " 
            self.mycursor.execute(query2, ) 
            details = self.mycursor.fetchall()
            for detail in details:  
                print (f"""
                ID: {detail[0]} 
                Name: {detail[1]}
                Email: {detail[2]}
                Password: {detail[3]}
                pin = {detail[4]}
                Phone_number: {detail[5]}
                Account_type: {detail[6]}
                Address: {detail[7]}
                kin:  {detail[8]}
                Account_no: {detail[9]}
                
    """) 
            self.staffdashboard() 
        except Exception as e:
            print(e) 
    def reg_detail(self): 
        try:  
            self.request = input("Enter customer account number: ").strip() 
        
        except ValueError: 
            print("Invalid")
            self.staffdashboard() 
        else:
            if len(self.request) <10 :
                print("Account does not exist") 
                self.staffdashboard() 
            else:
                query = "SELECT ID, fullname, email, password, phone_no, account_no, account_type, kin, address, account_balance, date_created FROM customer_table WHERE account_no = %s " 
                value = (self.request, ) 
                self.mycursor.execute(query, value ) 
                details = self.mycursor.fetchall()
                for detail in details:
                    print (f""" 
                    ID: {detail[0]} 
                    Name: {detail[1]} 
                    Email: {detail[2]}
                    Password: {detail[3]} 
                    Phone_number: {detail[4]} 
                    Account number: {detail[5]} 
                    Account Type: {detail[6]}
                    kin:  {detail[7]}
                    Address: {detail[8]}
                    Current Balance:$ {detail[9]}
                    Date Created: {detail[10]} 
                    
            """)
            time.sleep(1)
            opt = input("Press ENTER to continue and 1 to back")
            if opt == "1":
                    self.staffdashboard() 
            else:
                    self.reg_detail()
                
    def customer_tranc(self):
        print()
        try:
            self.account_no = int(input("Enter customer account number: ").strip()) 
        except ValueError:
            print("Invalid account")
        else: 
            query = "SELECT account_no, amount, transaction_type, sender_account, reciever_account, transaction_date FROM transaction_tables WHERE account_no = %s "
            value = (self.account_no, )  
            self.mycursor.execute(query, value) 
            details = self.mycursor.fetchall() 
            for detail in details:
                print(detail)
        
            time.sleep(1)
            opt = input("Press ENTER to continue and 1 to back: ") 
            if opt != "1": 
                self.customer_tranc() 
            else:
                self.staffdashboard()  

    def staff_profile(self):
            query = "SELECT ID, fullname, email, password, department, date_created FROM staff_table WHERE email = %s AND password = %s"
            value = (self.staff_email, self.staff_password ) 
            self.mycursor.execute(query, value) 
            details = self.mycursor.fetchall()
            for detail in details: 
                print(f"""
                        Staff ID: {detail[0]}
                        Name: {detail[1]}
                        Email: {detail[2]}
                        Password: {detail[3]}
                        Department: {detail[4]}
                        Creation Date: {detail[5]} 
                    """)
                self.staffdashboard()

    def create(self): 
        print('''
        Create your account here ----> 
        ''') 

        fullname = input("Full Name: ")
        email =input("Enter your email: ") 
        password = self.inputPassword() 
        pin = self.inputPin()  
        phone_no = input("Enter your Phone Number: ") 
        account_type = input("Account type: ")
        address = input("Enter your Address: ") 
        kin = input("Your next of kin: ")

        try: 
            query = "INSERT INTO customer_table(fullname, email, password, transaction_pin, phone_no, account_type, address, kin, account_no, account_balance) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            value = (fullname, email, password, pin, phone_no, account_type, address, kin, self.account_No, self.account_balance) 
            self.mycursor.execute(query, value)   
            
        except Exception as e:
            print(f"Something went wrong. {e}")  
        except:
            print("Email already exist, enter another email")
            self.create()
        else:
            print("Please wait while your account number is been generated...")
            time.sleep(1)
            print(f'''
            Congratulations {fullname} your account has been created successfully. 
            Your account number is {self.account_No}    
            
            Kindly Login to your account ----> 

            ''')      
            self.login()  
    def inputPassword(self):
        # password = (pw.pwinput()) 
        # confirm_password = (pw.pwinput()) 
        password = input('Password: ').strip()
        confirm_password = input('Confirm password: ') 
        if password == confirm_password: 
            return password 
        else:
            print('Password does not match') 
            self.inputPassword() 
    def inputPin(self): 
        pin = int(input('Set your 4 digit transaction pin: ').strip()) 
        confirm_pin = int(input('Confirm Pin: ').strip()) 
        if pin == confirm_pin:  
            return pin 
        else:
            print('Pin does not match')    
            self.inputPassword() 

    def login(self):
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ") 

        query2 = "SELECT fullname, email, password, account_balance, account_no FROM customer_table WHERE email = %s AND password = %s"
        value2 = (self.email, self.password ) 
        self.mycursor.execute(query2, value2) 
        details = self.mycursor.fetchall()
        try:
            self.customer_name = details[0][0]
            self.customer_email = details[0][1]
            self.customer_password = details[0][2] 
            self.customer_bal = details[0][3]
            self.customer_acct = details[0][4]
        except:
            print("Wrong email or password ") 
            user = input("Press ENTER to retry or 1 to go back to menu: ") 
            while user != "1":
                self.login()
            self.landingPage() 
        else:
            print(f'''  Welcome {self.customer_name} ({self.customer_acct})
                        Your account balance is ${self.customer_bal}''') 
            self.dashboard() 
              
    def dashboard(self):
        print(""" 
                    CUSTOMER DASHBOARD 
        1. Deposit                   
        2. Withdraw                 
        3. Transfer  
        4. Check balance  
        5. Pay bills                     
        6. Back
        7. Exit
        8. Check History
        0. Next 
        """)

        try:

            option = int(input('Your option: ')) 
        except ValueError:
            print("Invalid input") 
            self.dashboard()
        except Exception as e:
            print(f"Something went wrong {e}")

        else:
                
            if option == 1:
                self.deposit()
            elif option == 2: 
                self.withdraw()
            elif option == 3:
                self.transfer()
            elif option == 4:
                self.account_bal()   
            elif option == 5:
                self.bill() 
            elif option == 6:
                self.quit() 
            elif option == 7: 
                self.landingPage() 
            elif option == 0:
                self.dashboard2() 
            elif option == 8:
                self.history() 
            else:
                print("Invalid input")  
                self.dashboard() 

    def dashboard2(self):
        print("""           CUSTOMER DASHBOARD 
        1. Airtime 
        2. Buy data
        3. Check Profile
        4. Change Password
        5. Back
        6. Log out 
        7. Change transaction pin
              
            """)
        
        try:
            option = int(input('Your option: '))
        except ValueError:
            print("Invalid input")
            self.dashboard()
        except Exception as e:
            print(f"Something went wrong {e}")

        else:
            if option == 1:
                self.airtime()
            elif option == 2:
                self.data()
            elif option == 3:
                self.profile() 
            elif option == 4:
                self.updatepassword()
            elif option == 5:
                self.dashboard()
            elif option == 6:
                self.landingPage()
            elif option == 7:
                self.updatepin()
            else:
                print("Invalid Option")
                self.landingPage() 


    def profile (self):
        try:
            query = "SELECT fullname, email, password, transaction_pin, phone_no, account_type, address, kin, date_created FROM customer_table WHERE email = %s AND password = %s"
            value = (self.email, self.password ) 
            self.mycursor.execute(query, value)
            details = self.mycursor.fetchall()
            # print(details[0][2])
            print(f"""
                    Name: {details[0][0]}
                    Email: {details[0][1]}
                    Current Password: {details[0][2]}
                    Transaction pin: {details[0][3]}
                    Phone Number: {details[0][4]}
                    Account Type: {details[0][5]} 
                    Address: {details[0][6]}
                    Next of Kin: {details[0][7]}
                    Account Creation date: {details[0][8]}  
                    Branch of creation: {self.branch} 
                    Account Officer: Mr. Kane 
            """)
            self.dashboard2()
        except Exception as e: 
            print(f"Something went wrong. {e}") 
    def quit(self):
        exit() 
        
    def bill(self):
        print("""
                Pay bills
              1. Electricity bill 
              2. Cable TV
              3. Gaming and Gambling  
              4. Examination check pin
        """)
        option = input("Which bill are you paying for: ")
        if option == "1":
            self.electricity()
        elif option == "2":
            self.cable()
        elif option == "3":
            self.gaming()
        elif option == "4":
            self.exam() 
        else:
            print("Invalid choice....") 
            self.dashboard()

    def electricity(self):
        print("""
                Enter the region (IBEDC, IKEJA, SOKOTO, OGUN, ABUJA)
            """)
        region = input("Region: ").strip().upper()  
        query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value) 
        details = self.mycursor.fetchall() 
        get = details[0][1]
        print(details) 
        try:
            number = input(f"Enter the meter number:")
            user = float(input(f"Purchasing amount: ")) 
        except:
            print("Invalid Input")  
            self.electricity()  
        else: 
            if details[0][0] < user: 
                fund= input("Insufficient balance to purchase electricity bill! Try again.... press 1 to deposit ") 
                if fund == "1":
                    self.deposit()
                else:  
                    self.dashboard() 
            else:
                try:
                    pin = int(input("Enter your pin: "))
                except:
                    print("Error")
                else:
                    if pin == get:
                        time_now = dt.datetime.now()
                        ref = region 
                        query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account,reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
                        value2 = (self.customer_acct, user, "Electricity bill", self.customer_acct, self.customer_acct, ref, time_now)
                        self.mycursor.execute(query2, value2) 
                        new_bal = details[0][0] - user 
                        query1 = "UPDATE customer_table SET account_balance =%s WHERE password = %s"
                        value1 = (new_bal, self.password)
                        self.mycursor.execute(query1, value1)  
                        
                        time.sleep(1) 
                        print(f"${user} worth of electricity has purchased on {number} brnach {region} at {time_now}") 
                        time.sleep(1) 
                        print(f"""
                            transaction details
                            Amount: {user}
                            Type: Electricity bill  {region} 
                            From: {self.customer_acct} 
                            To: {number} 
                            Avail balance: {new_bal}  
                        """) 
                        time.sleep(1)
                        self.dashboard() 
    def cable(self):
        print("""
                Enter the TV to purchase (GOTV, DSTV, STARTIMES)
            """)
        cable = input("Cable TV: ").strip().upper()  
        query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value) 
        details = self.mycursor.fetchall() 
        get = details[0][1]
        print(details) 
        try:
            number = input(f"Enter the TV number:")
            user = float(input(f"Purchasing amount: ")) 
        except:
            print("Invalid Input")  
            self.cable() 
        else: 
            if details[0][0] < user:
                fund= input("Insufficient balance to purchase the Cable subscription! Try again.... press 1 to deposit ") 
                if fund == "1":
                    self.deposit() 
                else:  
                    self.dashboard() 
            else:
                try:
                    pin = int(input("Enter your pin: ")) 
                except:
                    print("error")
                else:
                    if pin == get:
                        time_now = dt.datetime.now() 
                        ref = cable 
                        query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account,reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
                        value2 = (self.customer_acct, user, "Cable bill", self.customer_acct, self.customer_acct, ref, time_now)
                        self.mycursor.execute(query2, value2) 
                        new_bal = details[0][0] - user 
                        query1 = "UPDATE customer_table SET account_balance =%s WHERE password = %s"
                        value1 = (new_bal, self.password)
                        self.mycursor.execute(query1, value1)  
                        
                        time.sleep(1) 
                        print(f"${user} worth of cable subscription has purchased on {number} at {time_now}") 
                        time.sleep(1) 
                        print(f"""
                            transaction details
                            Amount: {user}
                            Type: Cable TV  
                            From: {self.customer_acct}
                            To: {number} 
                            Avail balance: {new_bal}  
                        """)
                        time.sleep(1)
                        self.dashboard() 

    def gaming(self): 
        print("""
                Enter the game app to fund (SPORTY, BET9JA, PERIPESA, 1XBET)
            """)
        game = input("Sport App: ").strip().upper()  
        query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value) 
        details = self.mycursor.fetchall() 
        get = details[0][1] 
        print(details) 
        try:
            number = input(f"Enter the game ID:")
            user = float(input(f"Enter amount to fund: "))  
        except:
            print("Invalid Input")  
            self.cable() 
        else: 
            if details[0][0] < user: 
                fund= input("Insufficient balance to fund your game wallet! Try again.... press 1 to deposit ") 
                if fund == "1":
                    self.deposit()
                else:  
                    self.dashboard() 
            else:
                pin = int(input("Enter your pin: "))
                time_now = dt.datetime.now() 
                ref = game 
                if pin == get:
                    query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account,reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
                    value2 = (self.customer_acct, user, "Gaming fund", self.customer_acct, self.customer_acct, ref, time_now)
                    self.mycursor.execute(query2, value2) 
                    new_bal = details[0][0] - user 
                    query1 = "UPDATE customer_table SET account_balance =%s WHERE password = %s"
                    value1 = (new_bal, self.password)
                    self.mycursor.execute(query1, value1)  
                    
                    time.sleep(1) 
                    print(f"$Your game wallet {game} with ID {number} has been funded with {user} at {time_now}") 
                    time.sleep(1) 
                    print(f"""
                        transaction details
                        Amount: {user}
                        Type: Gamling fund  
                        From: {self.customer_acct}
                        To: {game}  {number} 
                        Avail balance: {new_bal}  
                    """)
                    time.sleep(1)
                    self.dashboard() 
                else:
                    print("Incorrect pin") 
                    self.dashboard() 
    def exam(self): 
        print("""
                Enter the Examination card you want to purchase (WAEC, NECO, GCE)
            """)
        exam_card = input("Exam card: ").strip().upper()  
        query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value) 
        details = self.mycursor.fetchall()
        get = details[0][1] 
        print(details) 
        try:
            print("""
                    2024: $2000
                    2023: $2500
                    2022: $3000
                    Others: $4000 
            """)
            year = int(input(f"Enter the year of examination:").strip()) 
            if year == 2024: 
                price = 2000
            elif year == 2023: 
                price = 2500
            elif year == 2022:
                price = 3000
            else:
                price = 4000 
            user = price  
        except:
            print("Invalid Input")  
            self.exam() 
        else: 
            if details[0][0] < user: 
                fund= input("Insufficient balance to purchase exam pin! Try again.... press 1 to deposit ") 
                if fund == "1":
                    self.deposit() 
                else:  
                    self.dashboard() 
            else:
                try:
                    pin = int(input("Enter your pin: "))
                    time_now = dt.datetime.now() 
                except ValueError:
                    print("Enter correct pin")
                else:
                    ref = exam_card  
                    if pin == get: 
                        query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account,reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
                        value2 = (self.customer_acct, user, "Examination Pin purchase", self.customer_acct, self.customer_acct, ref, time_now)
                        self.mycursor.execute(query2, value2) 
                        new_bal = details[0][0] - user 
                        query1 = "UPDATE customer_table SET account_balance =%s WHERE password = %s" 
                        value1 = (new_bal, self.password)
                        self.mycursor.execute(query1, value1) 
                        pin = random.randint(2200000, 2299999) 
                        
                        print(f"Wait while your PIN is generated.......") 
                        time.sleep(1) 
                        print(f"Your PIN is: >>> {exam_card}{year}/{pin}")  
                        time.sleep(1)
                        print(f"You have successfully purchased {exam_card} {year} PIN worth ${user} at {time_now}") 
                        time.sleep(1) 
                        print(f"""
                            transaction details
                            Amount: {user}
                            Type: Examination Pin  
                            From: {self.customer_acct} 
                            To: {exam_card}  {year} 
                            Avail balance: {new_bal}  
                        """)
                        time.sleep(1)
                        confirm = input("Do you want to purchase another pin? press ENTER to continue and 1 to quit")
                        if confirm == "1":
                            self.dashboard() 
                        else:
                            self.exam()  
                    else:
                        print("Incorrect pin")
                        self.dashboard() 

    def history(self):
        try:
            enter = self.customer_acct
            pass
        except ValueError:
            print("Incorrect account number") 
            self.dashboard() 
        except TypeError:
            print("Invalid")
        except Exception as e: 
            print(e)  
        else: 
            query = "SELECT account_no, amount, transaction_type, sender_account, reciever_account, transaction_date FROM transaction_tables WHERE account_no = %s "
            value = (enter, ) 
            self.mycursor.execute(query, value) 
            details = self.mycursor.fetchall() 
            for detail in details: 
                print(detail) 
            self.dashboard()

    def account_bal(self):  
        try:
            query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s" 
            value = (self.email, self.password ) 
            self.mycursor.execute(query, value)
            details = self.mycursor.fetchall() 
            get = details[0][1] 
            pin = int(input("Enter your pin: "))
            if pin == get:
                print("Please wait a moment....") 
                time.sleep(1) 
                print(f"Your account balance is ${details[0][0]}") 
                self.dashboard() 
            else:
                print("Incorrect pin")
                self.dashboard() 
        except Exception as e:
            print(f"Cannot fetch your balance at the moment. {e}") 

    def airtime (self):
        query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value) 
        details = self.mycursor.fetchall()
        get = details[0][1] 
        print(details) 
        try:
            user = float(input(f"Airtime amount: ")) 
            number = input(f"Input Phone number:") 
            Bonus = user*2
        except:
            print("Invalid Input")  
            self.airtime() 
        else: 
            if details[0][0] < user:
                print("Insufficient balance to purchase airtime! Try again... ")  
                self.dashboard() 
            else:
                time_now = dt.datetime.now() 
                try:
                    ref = input("Transaction reference: ") 
                    pin = int(input("Enter your pin: ")) 
                except:
                    print("error")
                else:
                    if pin == get:
                        query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account,reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
                        value2 = (self.customer_acct, user, "Airtime", self.customer_acct, number, ref, time_now)
                        self.mycursor.execute(query2, value2) 
                        new_bal = details[0][0] - user 
                        query1 = "UPDATE customer_table SET account_balance =%s WHERE password = %s"
                        value1 = (new_bal, self.password)
                        self.mycursor.execute(query1, value1)  
                        
                        time.sleep(1) 
                        print(f"${user} airtime has been credited to {number} at {time_now}. You have x2 bonus of your recharge {Bonus}")
                        time.sleep(1) 
                        print(f"""
                            transaction details 
                            Amount: {user}
                            Bonus: {Bonus}
                            Type: Airtime 
                            From: {self.customer_acct}
                            To: {number}
                            Avail balance: {new_bal} 
                        """)
                        time.sleep(1)
                        self.dashboard()  
                    else:
                        print("Incorrect pin")
                        self.dashboard()
        
    def data(self): 
        
        query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value) 
        details = self.mycursor.fetchall() 
        get = details[0][1] 
        print(details) 
        try:
            print(""" Data Plans 
                    1. 500Mb for $500
                    2. 1Gb for $1000
                    3. 2Gb for $1800
                    4. 5gb for $4500
                    5. 10Gb for $9000 
                    6. back
                  
                  """)
            user = int(input(f"Enter amount to purchase: ").strip()) 
            number = input(f"Input Phone number:") 
            bonus1 = user/2  
        except: 
            print("Invalid Input")   
            self.data()  
        else: 
            if details[0][0] < user: 
                print('''

                Insufficient balance to purchase data bundle! Try again... 

                ''')
                self.dashboard()  
            else: 
                if user == 500: 
                    comment = "You have successfully  purchase 500Mb worth of data"
                elif user == 1000:
                    comment = "You have successfully  purchase 1Gb worth of data" 
                elif user == 1800:
                    comment = "You have successfully  purchase 2gb worth of data"
                elif user == 4500:
                    comment = "You have successfully  purchase 5Gb worth of data"
                elif user == 9000:
                    comment = "You have successfully purchase 10Gb worth of data" 
                elif user == 6: 
                    self.dashboard2()
                time_now = dt.datetime.now() 
                try:
                    ref = input("Transaction reference: ") 
                    pin = int(input("Enter your pin: ").strip())
                except:
                    print("Error")
                else:
                    if pin == get:
                        query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account,reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
                        value2 = (self.customer_acct, user, "Airtime", self.customer_acct, number, ref, time_now)
                        self.mycursor.execute(query2, value2)  
                        new_bal = details[0][0] - user 
                        query1 = "UPDATE customer_table SET account_balance =%s WHERE account_no = %s" 
                        value1 = (new_bal, self.customer_acct) 
                        self.mycursor.execute(query1, value1)  
                        
                        time.sleep(1)
                        print(f"{comment} to {number} at {time_now}. You have a bonus of {bonus1}") 
                        time.sleep(1)
                        print(f"""
                            transaction details
                            Amount:  {user} 
                            Bonus: {bonus1} 
                            Type: Data  
                            From: {self.customer_acct} 
                            To: {number}
                            Avail balance: {new_bal} 
                        """)
                        time.sleep(1)
                        self.dashboard()   
                    else:
                        print("Incorrect pin")
                        self.dashboard() 


    def deposit(self):
        print ("""
    
        1. 1000                    
        2. 2000 
        3. 5000                    
        4. 10000
        5. Others                  
        6. Back 

        """)
        amount = {"1":1000.00, 
                  "2":2000.00, 
                  "3":5000.00, 
                  "4":10000.00} 

        user = input('Enter Your option: ')  

        
        if user == "5":
            try:
                process = float(input("Enter amount: "))
            except:
                print("Invalid input..")  
                self.deposit()
        elif user == "6":  
            time.sleep(1)
            self.dashboard() 
        else: 
            try:
                process = amount[user] 
            except:
                print("Invalid input..")
                self.deposit()

        query1 = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value1 = (self.email, self.password ) 
        self.mycursor.execute(query1, value1) 
        details = self.mycursor.fetchall()
        get = details[0][1]
        time.sleep(1)
        try:
            reference = input("Transaction reference: ") 
            pin = int(input("Enter your pin: ")) 
        except:
            print("Error")
        else:
            if pin == get:
                time_now = dt.datetime.now() 
                query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account, reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 

                value2 = (self.customer_acct, process, "Deposit",  self.customer_acct, self.customer_acct, reference, time_now)
                self.mycursor.execute(query2, value2) 
                
                new_balance = details[0][0] + process 

                query3 = "UPDATE customer_table SET account_balance =%s WHERE email = %s" 
                value3 = (new_balance, self.email)
                self.mycursor.execute(query3, value3)  
                
                print(f"${process} has been successfully deposited into your {self.account_No} at {self.time}, Your current available balance is ${new_balance}")

                time.sleep(1)
                print("""
                        Do you want to make another transaction?: 
                                                1. YES
                                                2. NO  
                """)
                option = input ("") 
                if option == "1":
                    self.deposit()
                elif option == "2":
                    self.dashboard()  
                else:
                    print("Invalid choice") 
                    self.login()
            else: 
                print("Incorrect pin") 
                self.dashboard() 

                        
    def withdraw(self): 
        
        print ("""
        1. 100                      
        2. 200
        3. 500                      
        4. 1000
        5. Others                   
        6. Back 

        """)
        amount = {"1":50.0, 
                  "2":100.0, 
                  "3":500.0, 
                  "4":1000.0} 

        user = input('Enter Your option: ')

        if user == "5":
            try: 
                process = float(input("Input amount: "))
            except:
                print("Invalid input..")
                self.withdraw()
        elif user == "6":  
            time.sleep(1)
            self.dashboard()
        else:
            try:
                process = amount[user] 
            except:
                print("Invalid input..")
                self.withdraw() 

        query = "SELECT account_balance, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value)
        details = self.mycursor.fetchall()
        print(details)
        get = details[0][1] 
        if process > details[0][0]:
            print("Insufficient fund") 
            self.dashboard() 

        else:
            new_bal = details[0][0] - process             
            time_now = dt.datetime.now() 
            try:
                reference = input("Transaction reference: ") 
                pin = int(input("Input your withdrawal pin: "))
            except:
                print("error") 
            else:
                if pin == get: 
                    query2 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type, sender_account, reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
                    value2 = (self.customer_acct, process, "Withdraw",  self.customer_acct, self.customer_acct, reference, time_now)
                    self.mycursor.execute(query2, value2)  

                    query1 = "UPDATE customer_table SET account_balance =%s WHERE email = %s" 
                    value1 = (new_bal, self.email)
                    self.mycursor.execute(query1, value1) 
                    print("Please wait while your transaction is processing....")  
                    time.sleep(1) 
                    print(f"You've successfully withdraw ${process} at {time_now}, Your account balance is ${new_bal}")
                    
                    time.sleep(1)
                    print("""
                        Do you want to make another transaction?:
                                                1. YES
                                                2. NO  
                    """)
                    option = input ("")
                    if option == "1":
                        self.withdraw() 
                    elif option == "2":
                        self.dashboard()  
                    else:
                        print("Invalid choice") 
                        self.login()    
                else:
                    print("incorrect pin")
                    self.dashboard() 
    def transfer(self):
        print("""   
                    1. Transfer to this bank
                    2. Transfer to other bank 
                    3. Back 
        """) 
        opt = input("Choice: ")
        if opt == "1":
            self.transfer_self()
        elif opt == "2":
            self.transfer_other()
        elif opt == "3":
            self.dashboard() 
        else:
            print("Invalid choice")
            time.sleep(1) 
            self.dashboard() 

    def transfer_self(self):  
        query = "SELECT account_no, fullname  FROM customer_table"
        self.mycursor.execute(query) 
        details = self.mycursor.fetchall() 

        print("Please wait...") 
        time.sleep(1) 

        time.sleep(1)
        user = input("Enter recipient account number: ").strip() 
        
        if user == self.customer_acct: 
            print("You cannot transfer to self(Account number).") 
            time.sleep(1)
            user = input("Press ENTER to retry or 1 to go back to menu: ")
            if user == "1":
                self.dashboard() 
            else:
                self.transfer() 
        else: 
            query = "SELECT account_balance, account_no, transaction_pin FROM customer_table WHERE email = %s AND password = %s" 
            val = (self.email, self.password ) 
            self.mycursor.execute(query, val)
            details = self.mycursor.fetchall()  
            get = details[0][2]

            query = "SELECT fullname, account_balance, account_no FROM customer_table WHERE account_no=%s"
            val = (user, ) 
            self.mycursor.execute(query, val) 
            details_2 = self.mycursor.fetchall()  
            try:
                amount = float(input(f"Amount to transfer ({user}): "))
                time.sleep(1)
                receiver = {details_2[0][0]} 
                print("Please confirm the name of the receiver")
                print(receiver) 
                ref = input("Reference: ")  
                pin = int(input("Enter your pin: ")) 
            except:
                print("Invalid input") 
                time.sleep(2)
                user_1 = input("Press ENTER to retry or 1 to go back to menu: ")
                while user_1 != "1": 
                    self.transfer() 
                self.dashboard()  
                
            else:
                if details[0][0] < amount: 
                    print("Insufficient balance")
                    time.sleep(1)
                    self.dashboard()
                else:
                    if pin == get:   
                        new_bal = details[0][0] - amount 

                        query3 = "UPDATE customer_table SET account_balance =%s WHERE account_no = %s" 
                        val3 = (new_bal, details[0][1]) 
                        self.mycursor.execute(query3, val3) 
                    
                        recipient_bal = details_2[0][1] + amount 
                        query4 = "UPDATE customer_table SET account_balance =%s WHERE account_no = %s"
                        val4 = (recipient_bal, user) 
                        self.mycursor.execute(query4, val4) 
                        
                        time.sleep(1)
                        time_now = dt.datetime.now() 

                        print(f"You've successfully transferred ${amount} to {details_2[0][0]} at {time_now}. Your account balance is ${new_bal}") 

                        query5 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type,  sender_account, reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                        val5 = (self.customer_acct, amount, "Transfer",  self.customer_acct, user, ref, time_now) 
                        self.mycursor.execute(query5, val5) 

                        time.sleep(1) 
                        self.dashboard()  
                    else:
                        print("Incorrect pin")
                        self.transfer() 

    def transfer_other(self):  
        query = "SELECT account_no FROM customer_table"  
        self.mycursor.execute(query) 
        info = self.mycursor.fetchall() 
        print("Please wait......")  
        time.sleep(1)   
        user = input("Enter recipient account number: ").strip() 
        
        if user == self.customer_acct: 
            print("You cannot transfer to self(account number)")
            time.sleep(1)
            user_1 = input("Press ENTER to retry or 1 to go back to menu: ")
            while user_1 != "1": 
                self.transfer() 
            self.dashboard()  
        else:  
            query2 = "SELECT account_balance, account_no, transaction_pin FROM customer_table WHERE email = %s AND password = %s"
            val2 = (self.email, self.password ) 
            self.mycursor.execute(query2, val2) 
            details = self.mycursor.fetchall()  
            get = details[0][2] 

            try:
                amount = float(input(f"Amount to transfer {user}:  "))
                ref = input("Reference: ")
                pin = int(input("Enter your pin: ")) 
            except:
                print("Invalid input")   
                time.sleep(2)
                user = input("Press ENTER to retry or 1 to go back to menu: ") 
                if user == "1": 
                    self.dashboard() 
                else: 
                    self.transfer() 
            else:
                if details[0][0] < amount: 
                    print("Insufficient balance")
                    time.sleep(1)
                    self.dashboard()
                else:
                    if pin == get:
                        new_bal = details[0][0] - amount 
                
                        query3 = "UPDATE customer_table SET account_balance =%s WHERE account_no = %s" 
                        val3 = (new_bal, details[0][1]) 
                        self.mycursor.execute(query3, val3) 
            
                        time.sleep(1)
                        time_now = dt.datetime.now() 
                        print(f"You've successfully transferred ${amount} to {user} at {time_now}. Your current account balance is ${new_bal}")

                        query5 = "INSERT INTO Transaction_tables (account_no, amount, transaction_type,  sender_account, reciever_account, reference, transaction_date) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                        val5 = (self.customer_acct, amount, "Transfer(Other)",  self.customer_acct, user, ref, time_now) 
                        self.mycursor.execute(query5, val5) 

                        time.sleep(1) 
                        opt = input("Press ENTER to perform another transaction and 1 to back to menu")
                        while opt != "1": 
                            self.transfer_other()
                        self.dashboard()  
                    else: 
                        print("Incorrect pin")
                        self.transfer() 

    def updatepassword(self): 
        pin = int(input("Enter your current password: ").strip()) 
        query = "SELECT password FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value)
        details = self.mycursor.fetchall()
        get = details[0][0] 
        if pin == get: 
            try:
                password = self.inputPassword() 
                query = ('UPDATE customer_table SET password=%s WHERE email = %s AND password = %s') 
                values = (password, self.email, self.password) 
                mycursor.execute(query, values) 
                print('Password updated successfully') 
                time.sleep(1)
                self.dashboard2() 
            except Exception as e:
                print(f"Something went wrong. {e}, please try again") 
                self.dashboard2()
        else:
            print("Incorrect pin")
            opt =input("Press ENTER to retry and 1 to back") 
            if opt == "1": 
                self.dashboard2()
            else:
                self.updatepassword() 
    def updatepin(self): 
        pin = int(input("Enter your current pin: "))
        query = "SELECT transaction_pin FROM customer_table WHERE email = %s AND password = %s"
        value = (self.email, self.password ) 
        self.mycursor.execute(query, value) 
        details = self.mycursor.fetchall()
        get = details[0][0] 
        if pin == get:        
            try:
                pin = self.inputPin() 
                query = ('UPDATE customer_table SET transaction_pin=%s WHERE email = %s AND password = %s') 
                values = (pin, self.email, self.password ) 
                mycursor.execute(query, values) 
                print('Pin updated successfully') 
                time.sleep(1)
                self.dashboard2() 
            except Exception as e:
                print(f"Something went wrong. {e}") 
        else:
            print("Incorrect pin") 
            opt =input("Press ENTER to retry and 1 to back") 
            if opt == "1":
                self.dashboard2()
            else:
                self.updatepin() 
    def forget_password(self): 
        try:
            self.user1 = (input("Enter your registered email: ")) 
            self.user2 = input("Enter your registered phone no: ") 
        except :
            print("Invalid details") 
            self.forget_password() 
        else:
            query = "SELECT email, phone_no FROM customer_table WHERE email = %s AND phone_no = %s" 
            value = (self.user1, self.user2 ) 
            self.mycursor.execute(query, value) 
            details = self.mycursor.fetchall() 
            for detail in details: 
                email = (detail[0])
                phone_num = (detail[1]) 
                if self.user1 == email: 
                    time.sleep(1)
                    print("Set a new password") 
                    passwd = self.inputPassword() 
                    query = ('UPDATE customer_table SET password=%s WHERE email = %s AND phone_no = %s')  
                    values = (passwd, self.user1, self.user2 ) 
                    mycursor.execute(query, values) 
                    print("Your password has been succesfully reset, you can proceed to login")
                    self.login() 
                elif self.user2 == phone_num: 
                    self.inputPassword() 
                else:
                    print("Invalid details") 

Mybank()     