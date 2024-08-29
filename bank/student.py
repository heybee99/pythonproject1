import csv 

all_scores = []


student_name = [] 
student_score =[]
student_grade = [] 

with open('student_grades.csv', 'r') as file:
    reader = csv.DictReader(file)  
    for rows in reader:
        if rows['Grade'] == 'A':
            with open('Grade_A.csv', 'a', newline='') as file2:
               writer = csv.writer(file2)
               writer.writerow([rows['Name'], rows['Score'], rows['Grade']])
        elif rows['Grade'] == 'B':
            with open('Grade_B.csv', 'a', newline='') as file2:
               writer = csv.writer(file2) 
               writer.writerow([rows['Name'], rows['Score'], rows['Grade']])
        elif rows['Grade'] == 'C':
            with open('Grade_C.csv', 'a', newline='') as file2:
               writer = csv.writer(file2) 
               writer.writerow([rows['Name'], rows['Score'], rows['Grade']])
        elif rows['Grade'] == 'D':
            with open('Grade_D.csv', 'a', newline='') as file2:
               writer = csv.writer(file2) 
               writer.writerow([rows['Name'], rows['Score'], rows['Grade']]) 
        elif rows['Grade'] == 'E':
            with open('Grade_E.csv', 'a', newline='') as file2:
               writer = csv.writer(file2) 
               writer.writerow([rows['Name'], rows['Score'], rows['Grade']]) 
        elif rows['Grade'] == 'F':
            with open('Grade_F.csv', 'a', newline='') as file2:
               writer = csv.writer(file2) 
               writer.writerow([rows['Name'], rows['Score'], rows['Grade']]) 
        

        

print(student_name) 
print(student_score)      
print(student_grade)  