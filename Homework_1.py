sizeArray_1 = int(input("Введите количество элементов 1 массива> "))
sizeArray_2 = int(input("Введите количество элементов 2 массива> "))
moreArraySize = 0

print("-" * 50)
numArray_1 = [int(input(f"[Array 1] Введите {i+1} елемент> ")) for i in range(sizeArray_1)]
print("-" * 50)
numArray_2 = [int(input(f"[Array 2] Введите {i+1} елемент> ")) for i in range(sizeArray_2)]
print("-" * 50)

common_numbers = list(set(numArray_1) & set(numArray_2))
common_numbers.sort()
print(common_numbers)



