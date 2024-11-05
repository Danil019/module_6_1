class Animal:
    alive = True  # Атрибут класса
    fed = False   # Атрибут класса

    def __init__(self, name):
        self.name = name  # Атрибут экземпляра

    def eat(self, food):
        if food.edible:  # Проверяем съедобность переданного объекта
            Animal.fed = True  # Обновляем атрибут класса fed
            print(f"{self.name} съел {food.name}")
        else:
            Animal.alive = False  # Обновляем атрибут класса alive
            print(f"{self.name} не стал есть {food.name}")


class Plant:
    edible = False  # Атрибут класса

    def __init__(self, name):
        self.name = name  # Атрибут экземпляра


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False  # Оставляем несъедобным


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Делаем съедобным


# Проверка работы программы
a1 = Predator("Волк с Уолл-Стрит")
a2 = Mammal("Хатико")
p1 = Flower("Цветик семицветик")
p2 = Fruit("Заводной апельсин")

print(a1.name)
print(p1.name)
print(Animal.alive)
print(Animal.fed)
a1.eat(p1)
a2.eat(p2)
print(Animal.alive)
print(Animal.fed)
