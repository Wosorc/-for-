
### 1. Список покупок
products = ["хлеб", "молоко", "яйца"]

products.append("сыр")
products.insert(0, "вода")
products.remove("молоко")

print("1. Список покупок:", products)

### 2. Средний балл
rating = [5, 4, 3, 5, 5, 4, 2]

sum = 0
ser = 0

for i in rating:
    sum += i

ser = sum / len(rating)

print("2. Средний балл:", sum, ser)

### 3. Максимум вручную
numbers = [17, -4, 32, 8, 32, 0, 15]

max = 0
maxIndex = 0

for number in numbers:
    if (number > max):
        max = number
        maxIndex = numbers.index(number)

print("3. Максимум вручную:", max, maxIndex)

### 4. Только чётные
numbers = [3, 8, 15, 22, 7, 10, 0, 41]

for number in numbers:
    if (number % 2 != 0):
        numbers.remove(number)

print("4. Только чётные:", numbers)

### 5. Циклический сдвиг
numbers = [1, 2, 3, 4]

temp = 0

print("5. Циклический сдвиг:", numbers)

### 6. Проверка сортировки
numbersOne = [1, 3, 3, 7, 9]
numbersTwo = [2, 5, 4, 8]
numbersThree = [6]

def VerisicationList (list):
    back = 0
    verisication = True

    for number in list:
        if (number < back):
            verisication = False
            break

        back = number

    return verisication

print("6. Проверка сортировки:", VerisicationList(numbersOne), VerisicationList(numbersTwo), VerisicationList(numbersThree))