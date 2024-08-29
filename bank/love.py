import random 

def home():
    user = (input("""Welcome to my love app........ press ENTER to play and 1 to quit"""))
    if user == "1": 
        home() 
    else:
        play()     
def play():
        check = random.randint(1, 100) 
        try:
            yourself = (input("Input your name: ").upper())
            partner = (input("Input your partner name: ").upper()) 
        except input == " ":
            print("Enter names")
            play()
        else:
            if  check <=100 and check >=80: 
                print(f"{yourself} and {partner} matched, you are destined to be together. You have {check}% match") 
                option = input("Press ENTER to continue and 1 to quit")
                if option == "1":
                    home()
                else:
                    play()
            elif check <=79 and check >=75:
                print(f"{yourself} and {partner} matched, hold yourself tight. You have {check}% match") 
                option = input("Press ENTER to continue and 1 to quit")
                if option == "1":
                    home()
                else:
                    play()
            elif check <= 74 and check >=65:
                print(f"{yourself} and {partner} matched but shine ya eye. You have {check}% match")
                option = input("Press ENTER to continue and 1 to quit") 
                if option == "1":
                    home()
                else:
                    play()
            elif check <=64 and check >=50: 
                print(f"{yourself} and {partner} are slightly matched. You have {check}% match")
                option = input("Press ENTER to continue and 1 to quit")
                if option == "1":
                    home()
                else:
                    play()
            elif check <=49 and check >=40: 
                print(f"{yourself} and {partner} do not matched, better find another partner. You have {check}% match")
                option = input("Press ENTER to continue and 1 to quit")
                if option == "1":
                    home()
                else:
                    play()            
            elif check <40:
                print(f"{yourself} and {partner} do not match at all, break up now or regret later!  You have {check}% match") 
                option = input("Press ENTER to continue and 1 to quit") 
                if option == "1":
                    home()
                else:
                    play() 
            else:
                print("Please input the name")  
                home()

home()
