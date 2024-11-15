numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

count = len(numbers)
index_None = numbers.index(None)
total = sum(numbers[:index_None] + numbers[index_None+1:])
average = total / count
numbers[4] = average
print("Измененный список:", numbers)
