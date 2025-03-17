'''

    if en cascada:
    estructura de control que permite
    evaluar varias condiciones en 
    cascada, es decir, si la primera
    condicion no se cumple, 
    se evalua la siguiente 
    y así sucesivamente.

'''
#ejemplo 1:
#Modificar el programa de votacion
#para que considere la edad de 17
#años 



edad = int(input("Ingresa su edad :"))
if edad >= 100:
    print("ya esta muy viejo para votar pero")
    res = input("¿Sigue vivo? (si/no)") 
    if res.strip().lower() == "si":
        print("Puede votar")
    else: 
        print("Descanse en Paz")
elif edad == 18: 
    print("Puedes votar")
elif edad == 17: 
    print("Puedes votar el proximo año")
elif edad < 17:
    print("No puedes votar aun")   
elif edad >= 10: 
    print("Usted es muy pequeño, que va a saber de politica")
elif edad >= 17:
    print("")     
print("Fin del programa")
