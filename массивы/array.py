def array_test():
    ar = [8, 3, 4, 5]

    ar.pop()

    ar.append(6)

    print(ar)
    print("Индекс 4:", ar.index(4)) # индекс заданного значения

    ar.remove(4) # удаляем первое появление элемента с заданным значением
    print("Удалили 4: ", ar)

    ar.reverse()
    print("Перевернутый массив: ", ar)
    print("Возвращаем отсортированый массив: ", sorted(ar))

    ar.sort()
    print("Отсортирован в начальное значение: ", ar)

def main():
    array_test()

if __name__ == "__main__":
    main()