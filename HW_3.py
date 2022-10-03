# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности в том же порядке.
# in 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
import random

def random_num(qwerty):
    ls_num = []
    for i in range(qwerty):
        ls_num.append(random.randint(1,10))
    return ls_num

def sort(abc):
    new_num = []
    j = 0
    while j < len(abc):
        if abc.count(abc[j]) < 2:
            new_num.append(abc[j])
        j += 1
    return new_num

numbers = int(input('Введите количество чесел: '))
exy = random_num(numbers)
print(exy)
print(sort(exy))