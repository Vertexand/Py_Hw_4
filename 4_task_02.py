# 2. задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

def f(num):
    list = []
    factor = 2
    while num > 1:
        if num % factor == 0:
            list.append(factor)
            num //= factor
        else:
            factor += 1
    return list
print(f(int(input('Введите натуральное число: '))))
