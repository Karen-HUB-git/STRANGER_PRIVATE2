import random

def выбрать_случайную_строку(PAS1k.txt):
    with open(путь_к_файлу, 'r', encoding='utf-8') as файл:
        строки = файл.readlines()
        случайная_строка = random.choice(строки)
        return случайная_строка

путь_к_вашему_файлу = 'PAS1k.txt'
случайная_строка = выбрать_случайную_строку(PAS1k.txt)
print(случайная_строка)
