# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randrange

def list(n: int):
    if n < 0:
        print("empty list!")
        return []

    list = []
    for i in range(n):
        list.append(randrange(n))

    return list


def unique(li: list):
    result = []
    dict = {}.fromkeys(li, 0)

    for i in li:
        dict[i] += 1

    for k in dict:
        if dict[k] == 1:
            result.append(k)

    return result

prin = list(int(input("Number of numbers, n: ")))
print(prin)
print(unique(prin))
