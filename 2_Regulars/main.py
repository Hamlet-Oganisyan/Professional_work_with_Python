import csv
import re
new_list = []
finish_list = []

with open("D:/Netology/Professional_work_with_Python/phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Функция , в которой приводим имена в соответствие
def names ():
    for x in contacts_list:  
        if len(x[0].split()) == 3:
            x[0] = x[0].split()
            x[1], x[2], x[0] = x[0][1], x[0][2], x[0][0]
        elif len(x[0].split()) == 2:
            x[0] = x[0].split()
            x[1], x[0] = x[0][1], x[0][0]
        elif len(x[1].split()) == 2:
            x[1] = x[1].split()
            x[2], x[1] = x[1][1], x[1][0]
        new_list.append(x)
names ()

# Функция , в которой ищем дубли по тмени и фамилии, при их нахождении дополняем информацию от друг у друга,
# избавляемся от дублей и лишних столбцов,
def dubles():
    for i in new_list:
            for j in new_list:
                if i[0] == j[0] and i[1] == j[1] and i is not j:
                    if i[2] == '':
                        i[2] = j[2]
                    if i[3] == '':
                        i[3] = j[3]
                    if i[4] == '':
                        i[4] = j[4]
                    if i[5] == '':
                        i[5] = j[5] 
                    if i[6] == '':
                        i[6] = j[6]
            ind = 0            
            for el in i:
                ind += 1
                if ind > 7:
                    i.remove(el)        
            if new_list.count(i) > 1: 
                new_list.remove(i)
dubles()

# Функция поиска номеров телефонов и их стандартизации
def regular():
    for row in new_list:
        text = ', '.join(row)
        pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
        result = re.sub(pattern, r'+7(\4)\8-\11-\14\15\17\18\20', text)
        print(result)
        finish_list.append([result])
regular()  

with open("D:/Netology/Professional_work_with_Python/2_Regulars/result_phonebook_raw2.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(finish_list)

 