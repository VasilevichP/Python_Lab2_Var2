li = []
while True:
    try:
        kod = int(input(
            "\nВыберите действие: "
            "\n1 - добавить элемент в список"
            "\n2 - вывести список на экран"
            "\n3 - посчитать число вхождений элемента в список"
            "\n4 - удалить элемент из списка по индексу\n"))
        if kod == 1:
            elem = int(input("Введите элемент: "))
            li.append(elem)
        elif kod == 2:
            if len(li)==0:
                print("\t\nСписок пуст")
            else:
                print(li)
        elif kod == 3:
            k=li.count(int(input("Введите искомый элемент: ")))
            if k!=0:
                print(k)
            else:
                print("\t\nНет такого элемента")
        elif kod == 4:
            ind = int(input("Введите индекс удаляемого элемента: "))
            try:
                del li[ind]
            except IndexError:
                print("\t\nНет элемента с таким индексом")
        else:
            print("Нет такого варианта")
    except ValueError:
        print("\t\nВведено нечисловое значение")
    except:
        print("\t\nВозникла неучтенная ошибка")
    finally:
        a = input('\t\nПродолжите работу или нажмите 0 для выхода из цикла: ')
        if a == '0':
            break
