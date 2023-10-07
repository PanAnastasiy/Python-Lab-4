from ColorLibraryOfLabWork_4 import *


def message():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '               ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ!              ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')


def menu():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '          СПИСОК ФУНКЦИЙ, РЕАЛИЗУЕМЫХ В ПРОГРАММЕ :       ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 1.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + " Задание 1 ( о классе List и его методах )              ",
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 2.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 2 ( о классах Alphabet и EngAlphabet )         ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 3.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 3 ( о классах PetShop и Animal, Fish, Bird )   ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 4.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 4 ( о классе Student и его методах )           ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 5.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 5 ( дополнительное задание )                   ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 6.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Выход из программы.                                    ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 7.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Информация о разработчике.                             ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' Введите номер подзадачи, которую желаете реализовать :   ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    return input()


def name_of_work():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED + '             ЛАБОРАТОРНАЯ РАБОТА №4',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + ' ВАРИАНТ 18           ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')


def info_of_developer():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE +
          '+---------------------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' ПРОГРАММА БЫЛА РАЗРАБОТАНА СТУДЕНТОМ 2 КУРСА :',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + ' ПАНФИЛЕНКО СТАНИСЛАВ ИГОРЕВИЧ ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE +
          '+---------------------------------------------------------------------------------+')
    name_of_work()
    print(Style.BRIGHT + Fore.BLUE +
          '+----------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ : ',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + ' stasa_stasa_stasa_stasa@mail.ru  ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE +
          '+----------------------------------------------------------------+')
