# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("Введите кол-во элементов множества: "))
my_set = input("Введите элементы массива через пробел: ")
elements = my_set.split()
array = [int(element) for element in elements]
print("Созданный массив:", array)
min = int(input("Введите минимум диапазона массива: "))
max = int(input("Введите максимум диапазона массива: "))
search_index = []
for i, element in enumerate(array):
    if min < element < max:
        search_index.append(i)
print("Номера индексов элементов в указанном диапазоне:", search_index)