COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
}


def get_mail(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            email = data[8]
            if search_value in email:
                id = data[0]
                phone = data[1]
                username = data[2]
                first_name = data[3]
                last_name = data[4]

                print(f'''{COLOR_CODE["RED"]}
╔══════                                               ══════╗
║                                                           ║
                {COLOR_CODE["RED"]}
                id пользователя {id}
                Номер телефона: {phone}
                Имя: {first_name}
                ФИО: {last_name}

                {COLOR_CODE["GREEN"]}
║                                                           ║
╚══════                                               ══════╝

                      ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR]Ничего не найдено в базе данных по почте.')

