# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10)
# многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
import random

k = int(input('Введите натуральную степень: '))
while k < 1:
    print('Вы ввели недопустимое число!!!!')
    k = int(input('Введите натуральную степень еще раз: '))
xaxa = '*x^'
znaki = [' + ',' - ']
mnogo4 = ''
while k != 0:
    num = random.randint(0, 10)
    if num != 0:
        znak = random.choice(znaki)
        mnogo4 = mnogo4 + str(num) + xaxa + str(k) + znak
    k -= 1
num = random.randint(0, 10)
mnogo4 = mnogo4 + str(num) + ' = 0'
print(mnogo4)
with open('mnogo.txt','a') as exy:
    exy.write(f'{mnogo4}\n')