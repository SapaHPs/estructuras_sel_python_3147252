'''
Operadores logicos

    Aquellos que operan únicamente
    con valores booleanos ("True" y "False")
    acorde a las tablas de Verdad

'''

# Ejemplo 1: Operador not: 

v = not True
print("El resultado de oprerar con 'not' es: ", v) 

# Ejemplo 2: Operador and: 

w = True and True
print("El resultado de oprerar con 'and' es: ", w)

# Ejemplo 3: Operador or:
x = False or False 
print("El resultado de oprerar con 'or' es: ", x)

'''

Jerarquía de presedencia de los operadores 
(logicos inclusive):

    1.          ()              ... => Aritméticos
    2.          **              ... => Aritméticos
    3.          *, /, %             ... => Aritméticos
    4.          +, -                ... => Aritméticos
    5.          <, >, <=, =>, !=, ==                ... => Comparativos
    6.          not             ... => Lógicos
    7.          and             ... => Lógicos
    8.          or              ... => Lógicos
    9.          =

'''

# Ejemplo 4: Jerarquía de operadores:

y = False and not True or False
print("El resultado de operar con Jerarquía de operadores es: ", y)  

# Ejemplo 5: Operadores relacionales y lógicos
z = not 3 > 4 and 4 == 4 or 3 < 2

print("El resultado de la operación con operadores relacionales y operadores lógicos es : ", z)

r = 3 + 5 * 2 > 3 and 4 == 4 or 3 < 2

print(r)

# Ejemplo 6: Ejemplo con paréntesis

d = (3+5 != 2 * 3) and 4 == 4 or not 3 < 2 
print(d)

q = (4**2 * 3 < 6 / (7 - 5)) and 7 * 2 + 1 == 14 or not 3 + 5 > 2 
print(q)