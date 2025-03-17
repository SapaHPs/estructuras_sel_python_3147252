'''

    Descripcion Actividad 2 :
    
    Elabore un programa en python 
    que determine si usted puede:
    
    A) casarse
    B) Comprometerse 
    C) Quedarce soltero/a
    
    Con base en las siguiente caracterizticas (variables):
    
    - estado civil (string = "soltero" o "casado", "comprometido")
    - edad (int)
    - temperamento (string = "buena persona, "mala persona")
    - fisico (string = "lindo/a", "feo/a")
    
'''

estado_civil = input("Ingrese su estado civil: (Soltero, Casado, Comprometido)")
edad = int(input("Ingrese su edad: "))
temperamento = input("Ingrese su temperamento: (Buena persona, Mala persona)")
fisico = input("Ingrese su físico: (Lindo/a, Feo/a)")
salario = int(input("Ingrese su salario: "))

if estado_civil.strip().lower() == "casado" or estado_civil.strip().lower() == "casada"or estado_civil.strip().lower() == "comprometido" or estado_civil.strip().lower() == "comprometida":
    print("No puedes acercarte a esa persona, ya tienes compromiso")
elif edad < 18:
    print("No puedes acercarte a esa persona, eres menor de edad")
elif temperamento.strip().lower() == "Mala persona":
    print("No puedes acercarte a esa persona, no es buena persona")
elif fisico.strip().lower() == "feo" or fisico.strip().lower() == "fea":
    print("No puedes acercarte a esa persona, no es atractivo/a")
elif salario < 1000000:
    print("No puedes acercarte a esa persona, no tienes suficiente dinero")
else:
    print("Puedes acercarte a esa persona")