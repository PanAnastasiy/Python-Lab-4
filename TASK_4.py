from ColorLibraryOfLabWork_4 import *

# Задание 4:
# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические методы, методы класса.


class Student:
    marks = [9, 9, 10, 9, 9, 9]

    def add_marks(self, *lst_of_marks):
        self.marks += lst_of_marks
        if len(list(filter(lambda x: not self.is_valid_mark(x), lst_of_marks))) != 0:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    'Была введена некорректная оценка!'
                                                    '\U0001f353\U0001f353\U0001f353')
        else:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nОценки студента : ', *lst_of_marks,
                  Style.BRIGHT + Fore.LIGHTGREEN_EX + 'были успешно добавлены.')

    def average_mark(self):
        try:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f'Средний балл студента равен '
                                                      f'{round(sum(self.marks)/len(self.marks), 3)}')
        except ZeroDivisionError:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    'Сведения о оценках студента отсутствуют!'
                                                    '\U0001f353\U0001f353\U0001f353')

    @staticmethod
    def is_valid_mark(mark):
        if 0 <= int(mark) <= 10:
            return True
        else:
            return False

    @staticmethod
    def print_student_info(first_name, second_name, middle_name, group_number, form_of_education):
        try:
            if len(group_number) != 6 and int(group_number):
                raise ValueError('Номер группы должен состоять из 6 символов и быть числом!')
            if not isinstance(form_of_education, bool):
                raise TypeError('Форма обучения должна быть булевым значением!')
        except ValueError as ve:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353' + str(ve) + '\U0001f353\U0001f353\U0001f353\n')
            return
        except TypeError as te:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353' + str(te) + '\U0001f353\U0001f353\U0001f353\n')
            return
        if form_of_education:
            form_of_education = 'БЮДЖЕТ'
        else:
            form_of_education = 'ПЛАТКА'

        print(Style.BRIGHT + Fore.LIGHTBLUE_EX +
              f'| {first_name.ljust(15 - len(first_name))} {second_name[0]}. {middle_name[0]}. |    {group_number}    |'
              f'     {form_of_education}     |\n'
              '+------------------+--------------+----------------+'
              )

    @classmethod
    def kind_of_student(cls):
        if len(list(filter(lambda x: x > 8, cls.marks))) == len(cls.marks):
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\nСтудент, обладающий такими оценками', *cls.marks,
                  Style.BRIGHT + Fore.LIGHTBLUE_EX + ' \033[4mОТЛИЧНИК\033[0m.')
        elif len(list(filter(lambda x: 9 < x > 6, cls.marks))) == len(cls.marks):
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\nСтудент, обладающий такими оценками', *cls.marks,
                  Style.BRIGHT + Fore.LIGHTBLUE_EX + ' \033[4mХОРОШИСТ\033[0m.')
        elif len(list(filter(lambda x: 7 < x > 4, cls.marks))) == len(cls.marks):
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\nСтудент, обладающий такими оценками', *cls.marks,
                  Style.BRIGHT + Fore.LIGHTBLUE_EX + ' \033[4mСРЕДНЕСТАТИСТИЧЕСКИЙ СТУДЕНТ\033[0m.')
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    '\nСтудента, обладающего такими оценками невозможно отнести '
                                                    'к какой-либо группе студентов'
                                                    '\U0001f353\U0001f353\U0001f353')


def task_4():
    Student.kind_of_student()
    print_static_method()
    my_student = Student()
    my_student.add_marks(8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10)
    my_student.average_mark()


def print_static_method():
    table_header()
    Student.print_student_info('Панфиленко', 'Станислав', 'Игоревич', '272302', True)
    Student.print_student_info('Пушкаревок', 'Илларий', 'Геннадьевич', '233401', False)
    Student.print_student_info('Вантусовик', 'Эдуард', 'Васильевич', '244401', True)
    Student.print_student_info('Базарова', 'Станислава', 'Игоревна', '233401', 'БЮДЖЕТ')
    Student.print_student_info('Романчук', 'Змея', 'Анатольевна', '2334014ty', True)


def table_header():
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '\n\n+------------------+--------------+----------------+\n'
          '|      СТУДЕНТ     | НОМЕР ГРУППЫ | ФОРМА ОБУЧЕНИЯ |\n'
          '+------------------+--------------+----------------+')
