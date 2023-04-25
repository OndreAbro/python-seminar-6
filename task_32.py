# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).


from random import randint


input_list = [randint(randint(-10, 0), randint(0, 20)) for i in range(randint(10, 20))]
print('Заданный массив: ', input_list)
try:
    left = int(input('Введите левую границу диапазона значений: '))
    right = int(input('Введите правую границу диапазона значений: '))
    if left > right:
        raise ValueError
    result_list = []
    for i in range(len(input_list)):
        if left <= input_list[i] <= right:
            result_list.append(i)
    print('Индексы принадлежащих диапазону элементов: ', result_list) if result_list else print('Таких элементов нет!')
except ValueError:
    print('Некорректный ввод данных!')
