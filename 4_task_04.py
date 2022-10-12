# Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import choice


def polynomial(num: int):
    if num < 1:
        return 0

    polyn = ""
    num_list = range(0, 100)

    with open("file02.txt", "w", encoding="utf-8") as my_f:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                polyn += f"{value}*x^{i} {choice('+-')} "

        my_f.write(f"{polyn}{choice(num_list)} = 0\n")# запись формулы в файл/38*x^3 - 19*x^2 - 64*x^1 + 56 = 0


for _ in range(2):# колич уравнен
    polynomial(int(input('enter degree, k:  ')))








