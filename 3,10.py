# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
num = int(input('Введите число: '))
def to_binary16(num):
    ans = ' '
    while num > 0:
        run = num % 16
        ans = str(run) + ans
        num //= 16
    return ans


print(to_binary16(num))
