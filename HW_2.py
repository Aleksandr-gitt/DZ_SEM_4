# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in 54
# out [2, 3, 3, 3]
# in 9990
# out [2, 3, 3, 3, 5, 37]
# in 650
# out [2, 5, 5, 13]

number = int(input('Введите число: '))
ls_num = []
num = 2
while num <= number:
    if number % num == 0:
        ls_num.append(num)
        number = number // num
    else:
        num += 1
print(ls_num)


#-----------------------------------------------------------------------
# Натуральные числа - числа которые делтся только на 1 и на сомо себя---
#-----------------------------------------------------------------------