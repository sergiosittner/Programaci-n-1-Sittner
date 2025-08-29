def convertir_minutos (minutos: int) -> None:
    hora = minutos// 60
    minutostotal = minutos % 60
    print(f"{minutos} minutos son: {hora} hora y {minutostotal} minutos")
