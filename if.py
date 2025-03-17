'''

    Estructura de contro, if: 
    Se utiliza para tomar decisiones 
    basadas en expresiones condicionles

'''

# Ejemplo 1: If simple

edad = int(input("Ingrese su edad aquí: "))

documento = input("¿Tienes numero de Documento? (si/no): ")

# Condicional: si la edad es mayor o igual a 18

if edad > 18  and documento.strip().lower() == "si":
    print("Eres mayor de edad y tienes documento, puedes votar")
else:
    print("Primero aprendase a limpiar la cola y luego se preocupa por la politica del país, mocos@. Y consigase un documento.")    

# Código que se ejecutará siempre

print("Fin del programa, vote por Petro, solo petro hp, la mala pa uribe y aguante Millos y la Changua, puro Bogota, la mala para medellin, gas la banjeda paisa solo changua con arroz, papa, ahuyama y los cubios.")