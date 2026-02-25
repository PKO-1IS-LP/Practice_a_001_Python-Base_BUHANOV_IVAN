def min2(a, b):
    
    if a < b:
        return a
    else:
        return b

def min3(a, b, c):
   
    min_ab = min2(a, b)
    result = min2(min_ab, c)
    return result

def min4(a, b, c, d):
    
   
    min_abc = min3(a, b, c)
    result = min2(min_abc, d)
    
    
    
    return result


print("Введите четыре числа:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())


print((min4(a, b, c, d)))