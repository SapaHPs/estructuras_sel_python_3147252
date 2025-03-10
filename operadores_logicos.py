'''
Operadores logicos

    Aquellos que operan únicamente
    con valores booleanos ("True" y "False")
    acorde a las tablas de Verdad

'''

# Ejemplo 1: Operador not: 

w = not True
print("El resultado de oprerar con 'not' es: ", w) 

# Ejemplo 2: Operador and: 

x = True and True
print("El resultado de oprerar con 'and' es: ", x)

# Ejemplo 3: Operador or:
y = False or False 
print("El resultado de oprerar con 'or' es: ", y)

'''

Jerarquía de presedencia de los operadores 
(logicos inclusive):

    1.          ()
    2.          **
    3.          *, /, %,
    4.          +, -
    5.          <, >, <=, =>, !=, ==
    6.          not
    7.          and
    8.          or
    9.          =

'''

# Ejemplo 4: Jerarquía de operadores:

z = False and not True or False
print("El resultado de operar con Jerarquía de operadores es: ", z)  