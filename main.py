from DescriptionOfLabWork_4 import *
from TASK_1 import *
from TASK_2 import *
from TASK_3 import *
from TASK_4 import *
from TASK_5 import *


def main():
    message()
    name_of_work()
    while True:
        your_choice = menu()
        match your_choice:
            case '1':
                task_1()
            case '2':
                task_2()
            case '3':
                task_3()
                pass
            case '4':
                task_4()
            case '5':
                task_5()
            case '6':
                print('\n' * 100)
                print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
                print(Style.BRIGHT + Fore.BLUE + '|',
                      Style.BRIGHT + Fore.RED + '             Осуществляем выход из программы...           ',
                      Style.BRIGHT + Fore.BLUE + '|')
                print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
                exit(0)
            case '7':
                print('\n' * 100)
                info_of_developer()
        if your_choice not in '1234567':
            print('\n' * 100)
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')
            print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
                  'Введённый вами номер задачи отсутствует в перечне функций. Повторите свой ввод.',
                  Style.BRIGHT + Fore.BLUE + '|')
            print(Style.BRIGHT + Fore.BLUE +
                  '+---------------------------------------------------------------------------------+')


main()
