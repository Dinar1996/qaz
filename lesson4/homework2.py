# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    tochka_position = str(number).find('.')
    celoe = str(number)[:tochka_position]
    drobnoe = str(number)[tochka_position+1:]

    drobnoe_left = drobnoe[0:ndigits]
    drobnoe_right = drobnoe[ndigits:ndigits+1]

    new_chislo = celoe + drobnoe_left

    if drobnoe_right and int(drobnoe_right) > 4:

        new_chislo = int(new_chislo) + 1
        new_chislo = str(new_chislo)


    new_chislo = new_chislo[0:tochka_position] + "." + new_chislo[tochka_position:]

    return new_chislo



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))