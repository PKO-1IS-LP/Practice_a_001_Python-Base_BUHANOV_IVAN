pol = 0
otr = 0
nul = 0

numbers = input("Введите числа через пробел: ").split()

for num_str in numbers:
    try:
        num = int(num_str)
        if num > 0:
            pol += 1
        elif num < 0:
            otr += 1
        else:
            nul += 1
    except ValueError:
        print(f"Ошибка! '{num_str}' не является целым числом и будет пропущено.")


print("Положительных:", pol)
print("Отрицательных:", otr)
print("Нулей:", nul)