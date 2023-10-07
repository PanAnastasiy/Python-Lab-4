from ColorLibraryOfLabWork_4 import *

# Задание 5:
# Требуется написать программу, которая  вычисляет общую площадь стены комнаты, которую необходимо оклеить обоями.
# При этом окна, двери, пол и потолок оклеивать не нужно.


class Room:
    def __init__(self, length, width, height):
        self.square_of_wallpaper = (length + width) * 2 * height

    def add_object(self, length, width):
        square = ObjectOfRoom(length, width).squareOfObject
        if self.square_of_wallpaper - square <= 0:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353'
                  f'Вы добавили слишком большой объект в свою комнату (площадь объекта {square}) '
                  'или же комната полностью заполнена объектами. '
                  'Обои уже не понадобятся('
                  '\U0001f353\U0001f353\U0001f353')
        else:
            self.square_of_wallpaper -= square
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nБыл добавлен объект в комнату площадью - ', square)


class ObjectOfRoom:
    def __init__(self, length, width):
        self.squareOfObject = length * width


def task_5():
    My_room = Room(20, 10, 5)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\nОбщую площадь стены комнаты, которую необходимо оклеить обоями :',
          My_room.square_of_wallpaper)
    My_room.add_object(15, 5)
    My_room.add_object(2, 11)
    My_room.add_object(3, 11)
    My_room.add_object(5, 5)
    My_room.add_object(8, 5)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОбщую площадь стены комнаты, которую необходимо оклеить обоями :',
          My_room.square_of_wallpaper)
    My_room.add_object(45, 5)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОбщую площадь стены комнаты, которую необходимо оклеить обоями :',
          My_room.square_of_wallpaper)
    My_room.add_object(8, 9)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОбщую площадь стены комнаты, которую необходимо оклеить обоями :',
          My_room.square_of_wallpaper)
