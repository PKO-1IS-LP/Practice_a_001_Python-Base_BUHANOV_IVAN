
g  = input("Введите числа через пробел: ")


numbers = list(map(int, g.split()))

max_even = None  

for num in numbers:
    if num % 2 == 0:  
        if max_even is None or num > max_even:
            max_even = num

# Выводим результат
if max_even is None:
    print("Нет чётных")
else:
    print("Максимальное чётное:", max_even)