n = int(input("Введите число"))
chet_chisl = 0
nechet_chisl= 0
for i in range(1, n + 1):
    if i % 2 ==0:
        chet_chisl+=1
    else:
         nechet_chisl +=1

print("Четных:",chet_chisl )
print("Нечетных:",nechet_chisl )