def buscar_mayor (numero1: int, numero2: int, numero3: int) -> None:
    lista = numero1, numero2, numero3
    ordenados = sorted(lista, reverse=True)
    print (f"los numeros en orden son:{ordenados}")
