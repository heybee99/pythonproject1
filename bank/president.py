import csv 
import os 
president_name = [] 
all_scores = []
# with open('president_height.csv', 'r') as file:
#     president_infos = file.readlines()
#     president_infos = president_infos[1:]  

#     for each in president_infos:
#         info_list = each.split(',')
#         president_name.append(info_list[1])
#         score = int(info_list[2].strip('\n'))
#         all_scores.append(score) 


with open('president_height.csv', 'r') as file: 
    reader = csv.DictReader(file) 
    for row in reader: 
        all_scores.append(int(row['height(cm)'])) 
        president_name.append(row['name'])  

print(president_name)  
print(all_scores)




