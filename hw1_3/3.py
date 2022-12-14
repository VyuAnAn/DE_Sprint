"""
Перевод арабского числа в римское

Дано целое положительное число X, необходимо вывести вариант этого числа в римской системе счисления в формате строки.
Римские числа записываются от наибольшего числа к наименьшему слева направо.
Однако число 4 не является “IIII”. Вместо этого число 4 записывается, как “IV”.
Т.к. 1 стоит перед 5, мы вычитаем 1, делая 4. Тот же принцип применим к числу 9, которое записывается как “IX”.
Случаи, когда используется вычитание:
I может быть помещен перед V и X, чтобы сделать 4 и 9.
X может быть помещен перед L и C, чтобы составить 40 и 90.
C может быть помещен перед D и M, чтобы составить 400 и 900.

Гарантируется, что введенное число X будет находиться в диапазоне от 1 до 2000
"""

rom = ["I", "V", "X", "L", "C", "D", "M"]


def get_rom(number):
    result = ''
    i = 0
    for value in str(number)[::-1]:
        if value in ["0", "1", "2", "3"]:
            result = rom[i] * int(value) + result
        if value in ["4"]:
            result = rom[i] + rom[i+1] + result
        if value in ["5", "6", "7", "8"]:
            result = rom[i+1] + (int(value) - 5) * rom[i] + result
        if value in ["9"]:
            result = rom[i] + rom[i+2] + result
        i += 2
    return result


# Пример 1: Вывод: “III”
print(get_rom(3))


# Пример 2: Вывод: “IX”
print(get_rom(9))


# Пример 3:Вывод: “MCMXLV”
print(get_rom(1945))
