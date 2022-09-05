# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class People:
    def __init__(self, name):
        self.name = name

class Student(People):
    def __init__(self, name,form, father, mother):
        super().__init__(name)
        self.form = form
        self.father = father
        self.mother = mother

ab = Student("Bob", "7 a", "Alex", "Julia")

class Teacher(People):
    def __init__(self, name,forms,predmet):
        super().__init__(name)
        self.forms = forms
        self.predmet = predmet

    def show_forms(self):
        for i in self.forms:
            print(i)

teacherone = Teacher("Victor",["5 a","7 a"],"russian")
teacherone.show_forms()



