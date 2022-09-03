import clr
clr.clrscr()
# Создали список строк, с которыми будем работать.
list_before_remove = []

# Прочитали текст из файла, поместили его в массив, закрыли исходный файл
fn = "Task1_input.txt"
f = open(fn, 'r')
list_before_remove = f.readlines()
f.close



list_after_remove = []
i = 0
for i in range(len(list_before_remove)):
    list_after_remove.append(list_before_remove[i].replace("абв", ''))
    i +=1

print(list_before_remove)
print(list_after_remove)
# Вывод обработанного текста в новый файл
fn = "Task1_output.txt"
f = open(fn, 'w')
i = 0
for i in range(len(list_after_remove)):
    f.write(list_after_remove[i])
    i += 1
f.close