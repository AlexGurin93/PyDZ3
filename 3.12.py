# 3.12 Вводим с клаиватуры строку.
# Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о" из исходной строки.
# Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.
stroka = input('Введите строку: ')
stroka = stroka.lower()
new_stroka = stroka.find('о')
if stroka.find('о') == 1:
    print(' обнаружена буква о')
if stroka.find('о') != 1:
    print('o не встречается')

# new_stroka = stroka[::-1]
# print(new_stroka)
# К сожалению, не знаю как развенуть строку между первой и второй.