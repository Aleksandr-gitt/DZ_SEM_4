# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл,
# содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!
#
with open('mnogo.txt','r') as xyz:
    aw = sum(1 for line in xyz)
with open('mnogo2.txt','r') as xyz2:
    wa = sum(1 for lne in xyz2)
if aw != wa:
    print("The contents of the files do not match!")
else:
    i = 0
    while i < aw:
        with open('mnogo.txt', 'r') as xyz:
            a = xyz.readlines()[i].strip()
        with open('mnogo2.txt', 'r') as xyz2:
            b = xyz2.readlines()[i].strip()
        i += 1
        a = a.replace("= 0", '+ ')
        c = a + b
        with open('new_mnogo4.txt', 'a') as new:
            new.write(f'{c}\n')

#--------------------------------------------------------------
# _________________ОПТИМИЗАЦИЯ_________________________________
# -------------------------------------------------------------

with open('mnogo.txt') as xyz, open('mnogo2.txt') as xyz2:
    aw = sum(1 for line in xyz)
    wa = sum(1 for lne in xyz2)
if aw != wa:
    print("The contents of the files do not match!")
else:
    i = 0
    xyz.seek(0)
    xyz2.seek(0)

    for i in range(aw):
        a = xyz.readline().replace("= 0\n", '+ ')
        b = xyz2.readline().strip()
        with open('new_mnogo4.txt', 'a') as new:
            new.write(f'{a + b}\n')
