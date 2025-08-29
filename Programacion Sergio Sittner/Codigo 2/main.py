from paquete.funciones import numero as nu
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))

func = int(input("Ingrese la función: ""\nSuma [1]\nResta [2]\nMultiplicación [3]\nDivisión [4]\n"))
match func:
    case 1:
        resultado = nu(numero1, numero2, func)
        print(f"el resultado es: {resultado}")   
    case 2:
        resultado = nu(numero1, numero2, func)
        print(f"el resultado es: {resultado}")
    case 3:
        resultado = nu(numero1, numero2, func)
        print(f"el resultado es: {resultado}")
    case 4:
        if numero1 and numero2 != 0:
            resultado = nu(numero1, numero2, func)
            print(f"el resultado es: {resultado}")
        else:
            print("No se puede dividir entre cero")
    case _:
        print("operación incorrecta")

        
    

    
    

