import os
import sys
import codecs
sys.path.append(r'.\lib')
import json

import create_data
import create_table
import pubs_info

settings = open('settings.json', 'r', encoding='utf-8')
settings = settings.read()
settings = json.loads(settings)

PUBS = settings['PUBS']
TOKEN = settings['TOKEN']

if __name__ == '__main__':
    print('Программа-скрипт для сбора информации о других аниме-пабликах. Команды:')
    print('1. create_data - создание первичной базы данных')
    print('2. create_table - создание удобной таблицы первичной базы данных')
    print('3. pubs_info - подробная информация о каждом паблике')
    print('4. Нажмите клавишу Enter для выхода')
    
    while 1:
        command = input('Введите команду: ')
    
        if command == 'create_data':
            create_data.create_data(PUBS, TOKEN)
            print('\nПервичная база данных создана')
        elif command == 'create_table':
            DATA = codecs.open(os.path.join(r'.\pub_info', 'data.json'), 'r', encoding='utf-8')
            create_table.create_table(DATA)
            print('\nПервичная таблица создана')
        elif command == 'pubs_info':
            DATA = codecs.open(os.path.join(r'.\pub_info', 'data.json'), 'r', encoding='utf-8')
            pubs_info.pubs_info(TOKEN, DATA)
            print('\nПодробная статистика пабликов создана')
        elif command == '':
            sys.exit()
        else:
            print('\nТакой команды не существует')