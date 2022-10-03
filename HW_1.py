# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

number = Decimal(input('Введите число: '))
accuracy = Decimal(input('Введите точность числа (например 0.001): ').replace(',','.'))
print(number.quantize(accuracy))

# ---------------------------------------------------------------------------
# Объекты Decimal имеют метод quantize(), который позволяет округлять числа.
# В этот метод в качестве первого аргумента передается также объект Decimal,
# который указывает формат округления числа
#----------------------------------------------------------------------------