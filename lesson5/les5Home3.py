# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
a = [1, 2 ,3, 4, 6]
b = []

for i in a:
    if i % 3 == 0:
        if i > 0:
            if i % 4 != 0:
                b.append(i)


print(b)
