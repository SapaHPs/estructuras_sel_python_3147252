motor_encendido = True

temperatura = int(input("cual es la temperatura del motor"))

if  temperatura > 80:
    motor_encendido = False
    print("La temperatura es alta, a continuacion se apagara el motor se apagará")
else:
    print("La temperatura es baja, el motor sigue encendido")
    
    