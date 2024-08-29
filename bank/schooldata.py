import mysql.connector as sql

mycon = sql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mainSchool_db" 
    )
mycursor = mycon.cursor()
mycon.autocommit = True 

class School: 
    def __init__(self, branch, location =None): 
        self.name = "Adex group of school"
        self.founder = 2001 
        self.branch = branch 
        self.location = location 
        self.data = {}
    def intro(self):   
        print(f"welcome to {self.name} branch of {self.branch} founded in {self.founder}")
    def homepage(self):
        print(f"welcome to {self.name} branch of {self.branch} branch")   

# mycursor.execute('CREATE TABLE Agric_exam_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, question VARCHAR(900), answer VARCHAR(20), course_code VARCHAR(20), admin_name VARCHAR(60), date_created DATETIME DEFAULT CURRENT_TIMESTAMP)')  
# mycursor.execute('CREATE DATABASE mainSchool_db')
# mycursor.execute('CREATE TABLE user_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, phone_no VARCHAR(11) UNIQUE, cgpa FLOAT(2) DEFAULT 5.0, department VARCHAR(20), isGraduate BOOLEAN DEFAULT FALSE, isAdmin BOOLEAN, isStudent BOOLEAN, password VARCHAR(20), date_created DATETIME DEFAULT CURRENT_TIMESTAMP)') 
# mycursor.execute('DROP TABLE user_table') 

# score = [] 
def home(): 
        user = input("""
            Welcome to the School Management System
        1. Login 
        2. Register
        #. Exit      
            
        Option:- """)
        if user == '1':
            login()
        else:
            register() 

def register():
        print('''
            Register as;
            1. Student
            2. Admin
            #. Exit
        ''')
        choice = input('Your Option: ') 
        if choice == '1':
            studentReg()
        elif choice == '2':
            adminReg()
        elif choice == '#': 
            exit()
        else:
            print('Invalid Choice') 
            register()

def studentReg(): 
        print('Student Registration') 
        try:
            fullname = input('Fullname: ')
            email = input('Email: ')
            phone_no = input('Phone Number: ')
            department = input('Course: ')
            password = inputPassword()
        except:
            print("Incorrect details")
        else:
            query = 'INSERT INTO user_table(fullname, email, phone_no, department, isStudent, password) VALUE(%s, %s, %s, %s, %s, %s)'
            values = (fullname, email, phone_no, department, True, password)
            mycursor.execute(query, values)
            print('Registeration Successfull, kindly proceed to login..')
            login()

def adminReg():
        print('Admin Registration')
        try:
            fullname = input('Fullname: ')
            email = input('Email: ')
            phone_no = input('Phone Number: ')
            department = input('Course: ')
            password = inputPassword()
        except:
             print("Incorrect details")
        else:
            query = 'INSERT INTO user_table(fullname, email, phone_no, department, isAdmin, password) VALUE(%s, %s, %s, %s, %s, %s)'
            values = (fullname, email, phone_no, department, True, password)
            mycursor.execute(query, values)
            print('Registeration Successfull, kindly proceed to login..')
            login()

def inputPassword():
        try:
            password = input('Password: ')
            confirm_password = input('Confirm Password: ')
        except:
            print("Incorrect details")
        else:
            if password == confirm_password: 
                return password
            else:
                print('Password does not match')
                inputPassword()

def login():
        print('Login here')
        try:
            email = input('Email: ').strip()
            password = input('Password: ').strip() 
        except:
            print("incorrect details")
        else:
            query = 'SELECT * FROM user_table WHERE email = %s AND password = %s'
            values = (email, password)
            mycursor.execute(query, values) 
            details = mycursor.fetchone() 
            # print(details)
            if details: 
                print('Login Successfully') 
                if details[7]: 
                    adminLogin(details)
                else:
                    studentLogin(details)

            else:
                print('Incorrect email or password')
                login()

def adminLogin(details):
        print(f'''
            Welcome {details[1]} 

        1. Set Test Questions 
        2. View Test Questions
        #. Exit 
        ''') 

        user = input("Your option: ")
        if user == "1":
             print("Welcome to set questions page")
             setExam()
        elif user == "2": 
             print("View your questions")
             viewQuest(details) 
        elif user == "#":
             print("Exit")
        else:
             print("Invalid option") 
             adminLogin(details)
             
def studentLogin(details):
        print(f'''
            Welcome {details[1]}
            
        1. Take Test 
        2. View Result 
        #. Exit
        ''')
        user = input("Your option: ")
        if user == "1":
            print("Welcome to test page")
            takeTest() 
        elif user == "2":
            print("Your test result.....")

def setExam():
    print("Set your questions and answer using your course code ")
    print('''Available courses to set 
          1. CSE 101
          2. ENG 101
          3. MTH 101
          4. CURRENT 101
          5. AGR 101
          ''')
    try:
        course_code = input('Course code: ').strip().upper() 
    except Exception as e:
        print(e)
    else: 
        if course_code == "CSE 101": 
            while True:
                    question = input('Question & Options: ').strip()
                    answer = input('Answer: ').strip().lower()
                    admin_name = input("Enter your name: ")
                    if question and answer:
                        query = 'INSERT INTO cseexam_table (question, answer, course_code, admin_name) VALUES (%s,%s,%s,%s)'
                        values = (question, answer, course_code, admin_name) 
                        mycursor.execute(query, values) 

                    user = input('Press ENTER to continue or 1 to stop: ')
                    if user == '1':
                        break
        if course_code == "ENG 101":
            while True:
                    question = input('Question & Options: ').strip()
                    answer = input('Answer: ').strip().lower()
                    admin_name = input("Enter your name: ").strip().lower()
                    if admin_name == "Ade":
                        if question and answer:
                            query = 'INSERT INTO engexam_table (question, answer, course_code, admin_name) VALUES (%s,%s,%s,%s)'
                            values = (question, answer, course_code, admin_name) 
                            mycursor.execute(query, values) 

                        user = input('Press ENTER to continue or 1 to stop: ')
                        if user == '1':
                            break
                    else:
                        print("Confirm your name or course you are setting")
        if course_code == "MTH 101":
            while True:
                    question = input('Question & Options: ').strip()
                    answer = input('Answer: ').strip().lower()
                    admin_name = input("Enter your name: ")
                    if question and answer:
                        query = 'INSERT INTO mathexam_table (question, answer, course_code, admin_name) VALUES (%s,%s,%s,%s)'
                        values = (question, answer, course_code, admin_name) 
                        mycursor.execute(query, values) 

                    user = input('Press ENTER to continue or 1 to stop: ')
                    if user == '1':
                        break
        if course_code == "CURRENT 101": 
            while True:
                    question = input('Question & Options: ').strip().upper()
                    answer = input('Answer: ').strip().lower()
                    admin_name = input("Enter your name: ")
                    if question and answer:
                        query = 'INSERT INTO exam_table (question, answer, course_code, admin_name) VALUES (%s,%s,%s,%s)'
                        values = (question, answer, course_code, admin_name) 
                        mycursor.execute(query, values) 

                    user = input('Press ENTER to continue or 1 to stop: ') 
                    if user == '1':
                        break
        if course_code == "AGR 101":
            while True:
                    question = input('Question & Options: ').strip() 
                    answer = input('Answer: ').strip().lower()
                    admin_name = input("Enter your name: ")
                    if question and answer:
                        query = 'INSERT INTO agric_exam_table (question, answer, course_code, admin_name) VALUES (%s,%s,%s,%s)'
                        values = (question, answer, course_code, admin_name) 
                        mycursor.execute(query, values) 

                    user = input('Press ENTER to continue or 1 to stop: ')
                    if user == '1':
                        break

def viewQuest(details): 
    name = details[1] 
    print('''View Question
          Enter your course code to view questions
          ''')
    try:
        course_code = input('Course code: ').upper().strip()
    except:
        print("Incorrect course code")
    else:
        if course_code == "CSE 101":
            print("Your set questions are....")
            mycursor.execute('SELECT * FROM cseexam_table') 
            details = mycursor.fetchall() 
            # print(details)
            for i in details:
                print(f'{i[0]}. {i[1]}\n Answer => {i[2]}' ) 
            print(f"Lecturer in charge=> {i[4]}") 
        elif course_code == "CURRENT 101":
            print("Your set questions are....")
            mycursor.execute('SELECT * FROM exam_table') 
            details = mycursor.fetchall() 
            for i in details:
                print(f'{i[0]}. {i[1]}\n Answer => {i[2]}' ) 
            print(f"Lecturer in charge=> {i[4]}")
        elif course_code == "ENG 101":
            print("Your set questions are....")
            mycursor.execute('SELECT * FROM engexam_table') 
            details = mycursor.fetchall() 
            for i in details:
                print(f'{i[0]}. {i[1]}\n Answer => {i[2]}' ) 
            print(f"Lecturer in charge=> {i[4]}")
        elif course_code == "MTH 101":
            print("Your set questions are....")
            mycursor.execute('SELECT * FROM mathexam_table') 
            details = mycursor.fetchall() 
            for i in details:
                print(f'{i[0]}. {i[1]}\n Answer => {i[2]}' ) 
            print(f"Lecturer in charge=> {i[4]}")
        elif course_code == "AGR 101":
            print("Your set questions are....")
            mycursor.execute('SELECT * FROM agric_exam_table') 
            details = mycursor.fetchall() 
            for i in details:
                print(f'{i[0]}. {i[1]}\n Answer => {i[2]}' ) 
                print(name) 
            print(f"Lecturer in charge=> {i[4]}")
        else: 
            print("Invalid") 
# Score = [] 
def takeTest(): 
    print('''
        Whcih course test are you taking
''') 
    try:
        test = input("Enter the course code: ")
    except:
        print("incorrect course code")
    else:
        if test == "AGR 101":
            mycursor.execute('SELECT * FROM agric_exam_table') 
            details = mycursor.fetchall() 
            for ques, anss in details:
                print(ques[1]) 
                #  print(ans[2])
                answer = input("Input your answer: ")
                if answer == ques[2]: 
                    print("Correct")
                else:
                    print(f"incorrect. The correct answer is {ques[2]}") 
        if test == "MTH 101":
            mycursor.execute('SELECT * FROM mathexam_table') 
            details = mycursor.fetchall() 
            for ques in details:
                print(ques[1]) 
                #  print(ans[2])
                answer = input("Input your answer: ")
                if answer == ques[2]: 
                    print("Correct")
                else:
                    print(f"incorrect. The correct answer is {ques[2]}") 
        if test == "CURRENT 101": 
            mycursor.execute('SELECT * FROM exam_table') 
            details = mycursor.fetchall() 
            for ques in details:
                print(ques[1]) 
                #  print(ans[2])
                answer = input("Input your answer: ")
                if answer == ques[2]: 
                    print("Correct") 
                else:
                    print(f"incorrect. The correct answer is {ques[2]}") 
        if test == "CSE 101":
            mycursor.execute('SELECT * FROM cseexam_table') 
            details = mycursor.fetchall() 
            for ques in details:
                print(ques[1]) 
                #  print(ans[2]) 
                answer = input("Input your answer: ")
                if answer == ques[2]: 
                    print("Correct")
                else:
                    print(f"incorrect. The correct answer is {ques[2]}") 
        Score = [] 
        if test == "ENG 101":
            mycursor.execute('SELECT * FROM engexam_table') 
            details = mycursor.fetchall() 
            for ques in details:
                print(ques[1]) 
                #  print(ans[2])
                answer = input("Input your answer: ")
                if answer == ques[2]: 
                    print("Correct")  
                    scores +=1 
                    # Score.append(scores)
                    
                else:
                    print(f"incorrect. The correct answer is {ques[2]}") 
    Score.append(scores)

    print(Score) 

  
home() 

