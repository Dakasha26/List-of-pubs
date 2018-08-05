# -*- coding: utf-8 -*-
import json
import codecs

f = open('table.html', 'w', encoding="utf-8")

tags_start = ['<html>', '<head>', '<meta charset="utf-8">', '<style>table{width: 1280px; text-align: center; margin: 0 auto;} tr{background: #d0d0d0;} .second{background: #f0f0f0;}</style>', '</head>', '<body>', '<table>', '<tr>', '<td>Номер паблика</td>', '<td>Имя паблика</td>', '<td>Ссылка на паблик</td>', '<td>Количество подписчиков</td>', '</tr>']
tags_end = ['</table>', '</body>', '</html>']
count = 1

for tag in tags_start:
    f.write('\n')
    f.write(tag)

with open('data.json', 'r', encoding="utf-8") as data:
    data = data.read()
    data = json.loads(data)

for el in data:
    if count % 2 == 0: 
        f.write("\n<tr class='second'><td>")
    else:
        f.write("\n<tr><td>")
    
    f.write(str(count))
    f.write("</td><td>")
    f.write(el["name"])
    f.write("</td><td>")
    f.write(el["href"])
    f.write("</td><td>")
    f.write(str(el["members_count"]))
    f.write("</td></tr>")
    count += 1

for tag in tags_end:
    f.write("\n")
    f.write(tag)
   
  
f.close()

print("Таблица создана")
input("Нажмите Enter для выхода")
