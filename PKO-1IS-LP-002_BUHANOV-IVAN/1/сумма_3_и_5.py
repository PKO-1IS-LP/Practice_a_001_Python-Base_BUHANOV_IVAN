n = int(input("Введите число: "))

total = 0

for i in range(1, n + 1):
    if i % 15 == 0:
        total += i

print("Сумма:", total)