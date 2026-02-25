s = input("Введите строку: ")

# Создаем копию строки и удаляем каждую цифру
result = s
for digit in '0123456789':
    result = result.replace(digit, '')

print(result)