from random import randint
from ColorLibraryOfLabWork_4 import *
import random

# Задание 3:
# Создать классы «Зоомагазин», «Животное», «Рыбы», «Птицы».
# Определить свойства: породу и стоимость для указанных животных (рыб, птиц)
# Вывести данные о самой дорогой породе.
# Предусмотреть метод записи информации в файл.


class PetShop:
    Animals = []

    def __int__(self, name):
        self.name_shop = name

    def add_animal(self, animal):
        self.Animals.append(animal)
        with open('Animals.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{animal.class_of_animal} {animal.cost} {animal.breed}\n')

    @classmethod
    def expensive_animal(cls):
        if cls.Animals:
            expensive_animal = max(cls.Animals, key=lambda animal: animal.cost)
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'Самая дорогая порода \033[4m{expensive_animal.breed}\033[0m',
                  Style.BRIGHT + Fore.LIGHTGREEN_EX + f'стоимостью '
                                                      f'\033[4m{expensive_animal.cost}\033[0m.')
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    'В магазине отсутствуют животные.'
                                                    '\U0001f353\U0001f353\U0001f353')

    @staticmethod
    def all_animals():
        with open('Animals.txt', 'r', encoding='UTF-8') as file:
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '+---------------------------------+\n'
                  '| КЛАСС | ЦЕНА |      ПОРОДА      |\n'
                  '+---------------------------------+')
            for line in file.readlines():
                info = line.strip().split()
                print(Style.BRIGHT + Fore.LIGHTCYAN_EX +
                      f'| {info[0].ljust(5)} |  {info[1].ljust(3)} | {info[2].ljust(17)}|\n'
                      '+---------------------------------+')


class Animal:

    def __init__(self, name):
        self.class_of_animal = name

    def ability(self):
        print('\033[4mТОП-ТОП\033[0m')


class Fish(Animal):

    def __init__(self, cost, breed):
        super().__init__('Рыба')
        self.__cost = cost
        self.__breed = breed

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        if cost > 0:
            self.__cost = cost
        else:
            self.__cost = randint(10, 100)

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, __breed):
        if len(__breed):
            self.breed = __breed
        else:
            self.cost = random.choice(['Красная шапочка', 'Телескоп', 'Комета', 'Золотая рыбка', 'Звёздочка'])

    def ability(self):
        print('\033[4mПЛЫВЁТ\033[0m')


class Bird(Animal):
    def __init__(self, cost, breed):
        super().__init__('Птица')
        self.__cost = cost
        self.__breed = breed

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        if cost > 0:
            self.__cost = cost
        else:
            self.__cost = randint(10, 130)

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, __breed):
        if len(__breed):
            self.breed = __breed
        else:
            self.cost = random.choice(['Красная шапочка', 'Телескоп', 'Комета', 'Золотая рыбка', 'Звёздочка'])

    def ability(self):
        print('\033[4mЛЕТАЕТ\033[0m')


def task_3():
    with open('Animals.txt', 'w') as file:
        file.truncate(0)
    Pet_House = PetShop()
    Pet_House.add_animal(Fish(10, 'Чёрная_глыба'))
    Pet_House.add_animal(Bird(130, 'Чёрный_Аист'))
    Pet_House.add_animal(Fish(24, 'Попрыгунья'))
    Pet_House.add_animal(Fish(10, 'Красная_ягода'))
    Pet_House.all_animals()
    Pet_House.expensive_animal()
