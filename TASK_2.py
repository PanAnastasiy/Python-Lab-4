from string import *
from ColorLibraryOfLabWork_4 import *

# Задание 2:
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два
# динамических свойства: 1) lang - язык и 2) letters - список букв. Начальные
# значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться
# родительский метод __init__(). В качестве параметров ему будут
# передаваться обозначение языка(например, 'En') и строка, состоящая из всех
# букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля
# string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет
# хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве
# параметра и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе он
# будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример
# текста на английском языке.


class Alphabet:
    def __init__(self, language, letters_of_alphabet):
        self.lang = language
        self.letters = tuple(letters_of_alphabet.lower())

    def print(self):
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nВесь алфавит имеет вид :', *self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', ascii_letters)

    def is_en_letter(self, letter):
        if letter.lower() in self.letters:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'\nЗаданная буква "{letter}" относится к английскому алфавиту.')
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    f'Заданная буква "{letter}" НЕ относится к английскому алфавиту.'
                                                    '\U0001f353\U0001f353\U0001f353')

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nПРИМЕР ТЕКСТА НА АНГЛИЙСКОМ : '
                                                  '\nPython is really better than another programming '
                                                  'languages such as C++. '
              'You must argue with this statement!')


#


def task_2():
    eng = EngAlphabet()
    eng.print()
    eng.example()
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nКоличество букв в АНГЛИЙСКОМ алфавите :', eng.letters_num())
    eng.is_en_letter('f')
    eng.is_en_letter('Q')
    eng.is_en_letter('ф')
    eng.is_en_letter('а')
