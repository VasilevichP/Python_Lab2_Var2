import math
import random


def fun(var):
    if isinstance(var, tuple):
        print("Количество элементов кортежа: ", len(var))
    elif isinstance(var, int):
        if var < 0:
            print('-',end='')
            var=int(math.fabs(var))
        print(str(var)[::-1])
    elif isinstance(var, list):
        if var[0] == 0:
            print("0 является первым элементом")
        else:
            try:
                print(sum(var[:var.index(0)]))
            except ValueError:
                print("В списке нет нулей")
    elif isinstance(var, str):
        print("Количество слов в строке:", len(var.split(" ")))
        most_common = var[0]
        number_of_appearances = sames = 0
        for i in var:
            if var.count(i) > number_of_appearances:
                most_common = i
                number_of_appearances = var.count(i)
                sames = 0
            elif var.count(i) == number_of_appearances and most_common != i:
                sames += 1
        if sames != 0:
            print("В строке несколько символов, встречающихся чаще всего")
        else:
            print("Самый часто встречающийся символ:", most_common)
    else:
        print("Нет операций с таким типом")


while True:
    print("\nВведите тип переменной или 0 для выхода:"
          "\n1 - Кортеж"
          "\n2 - Число"
          "\n3 - Список"
          "\n4 - Строка"
          "\n0 - Выход")
    while True:
        try:
            choice = int(input("Введите номер: "))
            break
        except ValueError:
            print("\tВведено нечисловое значение")
    if choice == 1:
        var = tuple([random.randint(0, 20) for i in range(random.randint(1, 16))])
        print(var)
        fun(var)
    elif choice == 2:
        var = random.randint(-9999999, 9999999)
        print(var)
        fun(var)
    elif choice == 3:
        var = [random.randint(0, 20) for i in range(random.randint(1, 16))]
        print(var)
        fun(var)
    elif choice == 4:
        var = input("Введите строку:")
        fun(var)
    elif choice == 0:
        break
    else:
        print("\tВВЕСТИ ЧИСЛО ОТ 0 ДО 4!!")
