# HOLA MUNDO

#print("Hola Mundo")

"""
a, b = 0, 1
while b<1000:
    print(b, end=',')
    a, b = b, a+b
"""
"""
x = int(input("Ingresa un entero, por favor: "))
if x < 0:
    x = 0
    print('Negativo cambiado a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Simple')
else:
    print('Más')
"""

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100) 