import random 
import time
import datetime 
from datetime import date 


def main_page():
    dtt = datetime.datetime.now().ctime() 
    print(dtt)
    print("""
                                            Welcome to my guess game app
        Which game would you like to play? 
          1. Letter guess
          2. Number guess 
          3. Fruit guess
          4. Animal guess 
    """)
    Option = input("Choose your choice: ")
    if Option == "1":
        letter_guess()
    elif Option == "2": 
        number_guess()
    elif Option == "3":
        fruit_guess()
    elif Option == "4":
        animal_guess()
    else:
        print("Invalid choice")

def fruit_guess(): 
    fruit = ["mango", "apple", "cashew", "pineapple", "orange", "banana", "watermelon"]
    print("Guess from the below fruits")
    for f in fruit: 
        print(f" {f}")
    secret_word = random.choice(fruit)
    print(secret_word)
    guess = "" 
    guess_count = 0 
    while guess != secret_word : 
        if guess_count <=2: 
            guess = input("Enter the guess word: ").strip().lower() 
            guess_count +=1
            if guess == secret_word: 
                print("You guess right........You won!")  
                break 
            else:
                print("Out of guesses, YOU LOSE!") 
                break 

def number_guess():
    number = random.randint(1,100) 
    guess = 0 
    print("Guess from number 1-100") 
    while guess != number: 
        try:
            guess = int(input("Enter Number Guess in the range of 100: ").strip())  
        except ValueError:
            print("Enter a number") 
        else:
            if (guess < number):
                print("Guess higher!") 
            elif (guess > number): 
                print("Guess lower!")
            else:
                print("Congratulations.....You won!") 

def letter_guess():
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print("Guess from A-Z")
    try:
        choosen = input("Enter your guess letter: ").strip().upper()
    except Exception as e:
        print(e)
    else:  
        choose = random.choice(choices) 
        if choosen == choose:
            print("You won")
        else:
            print("oouch! Wrong guess")
            print(f"The right guess is {choose}..... Try again!") 

def animal_guess():
        animal = ["cat", "dog", "goat", "cattle", "rabbit", "chicken", "giraffe", "lion", "tiger"]
        print(f"""Choose from this animals  
                    """) 
        for a in animal:
            print(a)
        secret_word = random.choice(animal) 
        print(secret_word)
        guess = ""
        guess_count = 0 
        while guess != secret_word: 
            if guess_count <=2: 
                try:
                    guess = input("Enter the guess word: ").strip().lower()
                except TypeError:
                    print("Enter from ")
                    guess_count +=1 
                    if guess == secret_word:
                        print("You guess right........You won!") 
                        press = input("Press ENTER to continue and 1 t0 quit") 
                        if press == "1":
                            main_page()
                        else:
                            animal_guess()
                    else:
                        print("Out of guesses, YOU LOSE!") 
                        animal_guess()

main_page()