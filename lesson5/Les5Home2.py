# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ["apple", "pear"]
b = ["banana", "peach", "apple"]
c = []
for i in a:
    for d in b:
       if i == d:
           c.append(i)
print(c)
