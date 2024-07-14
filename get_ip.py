import socket
import requests

COLOR_CODE = {
    "RESET": "\033[0m",
    "GREEN": "\033[32m",
    "RED": "\033[31m",  # Добавил ключ 'RED'
    "RED2": "\033[91m",  # Если 'RED' не подходит, добавьте новый ключ 'RED2' или выберите другой цвет
}

def get_ip():
    ip = input(f'{COLOR_CODE["RED"]}[@] Введите айпи: ')

    try:
        ip = socket.gethostbyname(ip)

        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()

        if infoList.get("success"):
            print(f'''{COLOR_CODE["RED2"]}
     ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
     ┃ IP:            {infoList["ip"]}
     ┃ Тип:           {infoList["type"]}
     ┃ Страна:        {infoList["country"]}
     ┃ Регион:        {infoList["region"]}
     ┃ Город:         {infoList["city"]}
     ┃ Почтовый индекс:  {infoList["postal"]}
     ┃ Столица страны:       {infoList["capital"]}
     ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
''')
        else:
            print(f'''{COLOR_CODE["GREEN"]}
╔══════════════                     ══════════════╗
     [+] IP:           {infoList["ip"]}
     [+] Success:      {infoList["success"]}
     [+] Message:      {infoList["message"]}
╚══════════════                     ══════════════╝
''')
    except Exception as e:
        print(f'{COLOR_CODE["GREEN"]}Ошибка, обратитесь к автору @STR3ANGER": {e}')
