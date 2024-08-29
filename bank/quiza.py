NoOfStudents = int(input("Number of students: ")) 
Students = [] 
for students in range(NoOfStudents): 
    name = input(f"Enter name of students {students+1}: ")
    Students.append(name)
for each in Students:
    # print(f"Welcome {each}") 
    print("")
for each in range(students): 
    print((f"welcome {Students[0]}")) 
Questions = ("How many elements are in the periodic table",
             "Which of these is not a United players",
             "How many state is in Nigeria",
             "Where is river niger located")

Options = (( "A. 114", "B. 122", "C. 333", "D.123"), 
           ("A. rashford", "B. bale", "C. bruno", "D. shaw"),
           ("A. 34", "B. 36", "C. 44", "D. 55"),
           ("A. oyo", "B. cross river", "C. kwara", "D. osun") 
           )

Answer = ("B", "B", "B", "B")
Guesses = []
Score = 0
QuestionsNum = 0  

for question in Questions: 
    print(".................................")
    print(question)
    for option in Options[QuestionsNum]: 
        print(option)
    guess = input("Enter (A, B, C, D):").upper() 
    Guesses.append(guess)
    if guess == Answer[QuestionsNum]: 
        Score += 1
        print("CORRECT") 
    else:
        print("INCORRECT") 
        print(f"{Answer[QuestionsNum]} is the correct answer") 
    QuestionsNum +=1 

print("/////////////////////////////////////////") 
print("RESULTS")
print("/////////////////////////////////////////") 


print("answers:")
for answer in Answer: 
    print(answer)
print()

print("guesses:")
for guess in Guesses: 
    print(guess)
print()

Score = int(Score/len(Questions)*100) 
print(f"Your score is {Score} %")  