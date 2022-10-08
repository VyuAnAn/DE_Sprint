"""
Умножить два бинарных числа в формате строк
На вход подаются две строки X1 и X2, содержащие бинарные числа.
Необходимо вывести их бинарное произведение в формате строки.

Пояснение: “111” - это 7; “101” - это 5; 7*5 = 35; 35 в двоичной системе 100011
Гарантируется, что введенная строка X будет содержать только числа 1 и 0.
"""


def bin_to_dec(number):
    l = len(number)
    dec = 0
    for i in range(0, l):
        dec = dec + int(number[i])*(2**(l-i-1))
    return dec


def get_result(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


# Пример 1: Вывод: “100011”
x1 = "111"
x2= "101"

print(bin_to_dec(x1))
print(bin_to_dec(x2))

x = bin_to_dec(x1)
y = bin_to_dec(x2)
z = x*y
print(get_result(z))