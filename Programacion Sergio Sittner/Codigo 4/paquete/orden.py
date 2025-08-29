def buscar_mayor (numero1: int, numero2: int, numero3: int) -> None:
        
        
        if numero1 > numero2 and numero1 > numero3:
            if numero2 > numero3:

                print(f"numeros ordenados: {numero1}, {numero2}, {numero3}.")
            
            else:
                print(f"numeros ordenados: {numero1}, {numero3}, {numero3}.")
          
        if numero2 > numero1 and numero2 > numero3:
            if numero1 > numero3:
                print(f"numeros ordenados: {numero2}, {numero1}, {numero3}.")

            else:
                print(f"numeros ordenados: {numero2}, {numero3}, {numero1}.")

            
        if numero3 > numero1 and numero3 > numero2:
            if numero1 > numero2:
                print(f"numeros ordenados: {numero3}, {numero1}, {numero2}.")

            else:
                print(f"numeros ordenados: {numero3}, {numero2}, {numero1}.")

            



