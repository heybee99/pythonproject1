
def home():
    print("Welcome to my grading system......... press ENTER to play and 1 to quit")
    user = input("Option:   ")
    if user == "1":
        home()
    else:
        play()     
def play():
    try:
        no = int(input ("Please enter number: ")) 
        if no <=100 and no >=80:
            print("Excellect result") 
        elif no <=79 and no >=75:
            print("A grade") 
        elif no <= 74 and no >=65:
            print("B grade") 
        elif no <=64 and no >=50: 
            print("C grade")
        elif no <=49 and no >=40:
            print("D grade") 
        elif no <40:
            print("F grade") 
        else:
            print("Check the number again! The number is higher than 100 ")
            home()
        play()
    except ValueError:
        print("Enter a correct number") 
        play()
    except Exception as e:
        print(f"Something went wrong {e}") 


