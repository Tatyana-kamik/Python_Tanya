lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Фильтрация элементов списка
filtered_elements = [
    num for num in lst if num < 30 and num % 3 == 0
]

# Вывод отфильтрованных элементов
print(filtered_elements)