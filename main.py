import os
import random
import time
from pystyle import Colorate, Colors
from colorama import Fore, init

banner2 = '''
███████████████████████████████████████████████████████████████████████████████
█                                                                             █
                                                                              █
  ░██████╗████████╗██████╗░██████╗░░█████╗░███╗░░██╗░██████╗░███████╗██████╗░
  ██╔════╝╚══██╔══╝██╔══██╗╚════██╗██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗
  ╚█████╗░░░░██║░░░██████╔╝░█████╔╝███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
  ░╚═══██╗░░░██║░░░██╔══██╗░╚═══██╗██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
  ██████╔╝░░░██║░░░██║░░██║██████╔╝██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝
█                           @STR3ANGER                          RIVATE v2     █
███████████████████████████████████████████████████████████████████████████████              
╔=====================================================================╗
║[1] DDos сайта                      [5] Генератор паспортов          ║
║[2] Пробив по IP                    [6] Пробив по id телеграм        ║                                     
║[3] Пробив по почте                 [7] Парсинг сайтов(скоро)        ║
║[4] Пробив по номеру телефона       [8] Выйти из скрипта             ║
╚=====================================================================╝  
'''

print(Colorate.Horizontal(Colors.yellow_to_red, banner2))

def get_id(путь_к_файлу, значение_поиска, цвета):
    with open(путь_к_файлу, 'r', encoding='utf-8') as файл:
        for строка in файл:
            if значение_поиска in строка:
                данные = строка.strip().split(';')
                for индекс, значение in enumerate(данные, start=1):
                    значение = значение.strip()
                    if значение:  # Проверяем, что значение не пусто после удаления пробелов
                        print(f'{цвета["PURPLE"]}[{индекс}] {цвета["RESET"]}{значение}')


# Определите функцию генерации паспорта
def сгенерировать_паспорт():
    # Используйте выбрать_случайную_строку для случайного выбора строки из файла
    путь_к_вашему_файлу = 'PAS1k.txt'
    случайная_строка = выбрать_случайную_строку(путь_к_вашему_файлу)
    return случайная_строка

# ... (остальной код) ...


def выбрать_случайную_строку(путь_к_файлу):
    with open(путь_к_файлу, 'r', encoding='utf-8') as файл:
        строки = файл.readlines()
        случайная_строка = random.choice(строки)
        return случайная_строка

COLOR_CODE = {
    "PURPLE": "\033[35m",
    "BOLD": "\033[01m",
    "RESET": "\033[0m",
    "GREEN": "\033[32m",
    "YELLOW": Fore.YELLOW,
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BLUE": "\033[34m",
}

prompt_text = f'{COLOR_CODE["PURPLE"]}[+]{COLOR_CODE["BOLD"]} Выберите опцию'
final_prompt = f"{prompt_text}{COLOR_CODE['PURPLE']} > {COLOR_CODE['RESET']}"

select = input(final_prompt)

if select == '1':
    from ddos import dos
    dos()
    input("Нажмите Enter, чтобы продолжить...")

elif select == '2':
    from get_ip import get_ip
    get_ip()
    input("Нажмите Enter, чтобы продолжить...")

elif select == '3':
    from gmail import get_mail
    database_file = 'Nathack.csv'  # Заменяем на файл Nathack
    search_value = input(f'{COLOR_CODE["YELLOW"]}[@] Введите почту:')
    get_mail(database_file, search_value)

elif select == '4':
    from telefon import get_number

    # Заменяем на список всех нужных баз данных
    database_files = ['STR3ANGER(AKUMA BD).csv', 'STR3ANGER.csv', 'STR3ANGER(NATHACK_BD).csv']

    search_value = input(
        '{}Введите номер телефона (формат: 79999999999): {}'.format(COLOR_CODE["GREEN"], COLOR_CODE["RESET"]))

    # Ищем в каждой базе данных
    for database_file in database_files:
        get_number(database_file, search_value, COLOR_CODE)



elif select == '5':
        количество_паспортов = min(1000, int(input("Введите количество паспортов для генерации (максимум 1000): ")))
        for _ in range(количество_паспортов):
            сгенерированный_паспорт = сгенерировать_паспорт()
            print(сгенерированный_паспорт)

    # ... (ваш код выбора опций) ...
elif select == '6':
        from telefon import get_number

        # Заменяем на список всех нужных баз данных
        database_files = ['STR3ANGER(AKUMA BD).csv', 'STR3ANGER.csv', 'STR3ANGER(NATHACK_BD).csv']

        search_value = input(
            '{}Введите id telegram: {}'.format(COLOR_CODE["GREEN"], COLOR_CODE["RESET"]))

        # Ищем в каждой базе данных
        for database_file in database_files:
            get_id(database_file, search_value, COLOR_CODE)

        input("Нажмите Enter, чтобы продолжить...")
elif select == '7':
        print("Накодится в стадии разработки")

elif select == '8':
        exit()

else:
        print(f'{COLOR_CODE["RED"]}Неверный выбор, попробуйте снова!{COLOR_CODE["RESET"]}')

