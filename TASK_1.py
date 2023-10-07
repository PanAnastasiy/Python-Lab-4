from ColorLibraryOfLabWork_4 import *

# Задание 1:
# Создать класс List (список), в котором реализовать методы для работы со
# списком (не менее 5).


class List:
    data = []

    def add_element(self, element):
        self.data.append(element)

    def find_element(self, element):
        if element in self.data:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'\nИндекс элемента {element} в массиве :',
                  self.data.index(element))
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    f'Заданный вами элемент {element} отсутствует в списке.'
                                                    '\U0001f353\U0001f353\U0001f353')

    def del_element_index(self, index):
        if index in self.data:
            del self.data[index]
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'\nЗаданный вами элемент по индексу {index} был удален.')
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    f'Заданный вами элемент по индексу {index} отсутствует в списке.'
                                                    '\U0001f353\U0001f353\U0001f353')

    def get_length(self):
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nДлина списка равна :', len(self.data))

    def del_element(self, element):
        if element in self.data:
            self.data.remove(element)
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'\nЗаданный вами элемент {element} был удален.')
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    f'Заданный вами элемент {element} отсутствует в списке.'
                                                    '\U0001f353\U0001f353\U0001f353')


def task_1():
    My_list = List()
    for i in range(10):
        My_list.add_element(i)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nСписок имеет вид : ', My_list.data)
    My_list.find_element(5)
    My_list.find_element(11)
    My_list.get_length()
    My_list.del_element_index(2)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nСписок имеет вид : ', My_list.data)
    My_list.get_length()
    My_list.del_element(6)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nСписок имеет вид : ', My_list.data)
    My_list.del_element(10)
    My_list.del_element_index(15)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nСписок имеет вид : ', My_list.data)
