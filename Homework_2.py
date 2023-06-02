n = int(input("Введите количество кустов> "))

berries = list()

for i in range(n):
    berries.append((int(input("Введите количество ягод> "))))

arr_count = list()

for i in range(len(berries) - 1):
    arr_count.append((berries[i - 1] + berries[i] + berries[i+1]))
arr_count.append(berries[-2] + berries[-1] + berries[0])

print(max(arr_count))