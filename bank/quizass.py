studentNumber = int(input("How many student are you registering: "))
students = []
for i in range(studentNumber):
    name = input(f"Register students here {i+1} name: ")
    students.append(name)
allScores = []
Questions = [
    "1. How many elements are in the periodic table a.) 230 b.) 450",
    "2. Which of these are United players a.) rash b.) bass",
    "3. How many state is in Nigeria a.) 35 b.) 36",
    "4. Where is river niger located a.) river state b.) osun",
    ]
Answers = ["b", "b", "b", "b"] 
# print(Questions) 
for student in students:
    print(f"Welcome {student} to the test ")
    score = 0
    for question, answer in zip(Questions, Answers):
        print(question)
        user = input("Answer: ").lower()
        if user == answer:
            print("Correct!")
            score += 1 
        else:
            print("Incorrect!")
            # print("The correct answer is {answer}")
    allScores.append(score) 
    
print(f" Student names {students} scored {allScores} ")
print("/////////////////////////////////")
print(f" The minimum score is {min(allScores)} and its scored by {min(students)}") 
print("/////////////////////////////////")
print(f" The maximum score is {max(allScores)} and its scored by {max(students)} ") 
print("/////////////////////////////////")


print(f"Answers Overview{Answers}")
