COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}


def id(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if search_value in phone:
                id = data[0]
                phone = data[1]
                username = data[2]
                first_name   = data[3]
                last_name = data[4]


                print(f'''{COLOR_CODE["RED"]}
╔══════                                               ══════╗
║                                                           ║
                {COLOR_CODE["RED"]}[+]
               [>]ID пользователя: {id}
               [>]Тег: {username}
               [>]Имя: {last_name}
               [>]ФИО: {first_name}
                

                {COLOR_CODE["GREEN"]}
║                                                           ║
╚══════                                               ══════╝

                      ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR]Ничего не найдено в базе данных по номеру телефона.')

