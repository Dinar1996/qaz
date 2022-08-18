# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    is_lucky = True

    if len(ticket_number) !=6:
        is_lucky = False
    else:
        left_part = ticket_number[0:3]
        right_part = ticket_number[3:]


        summ_left = 0
        summ_right = 0

        left_part = int(left_part)
        right_part = int(right_part)

        first_number = left_part // 100
        second_number = (left_part - first_number * 100) // 10
        third_number = left_part -first_number * 100- second_number * 10
        sum_left = first_number + second_number + third_number

        first_number = right_part // 100
        second_number = (right_part - first_number * 100) // 10
        third_number = right_part - first_number * 100 -second_number * 10
        sum_right = first_number + second_number + third_number



        if sum_left != sum_right:
            is_lucky = False

    return is_lucky

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))