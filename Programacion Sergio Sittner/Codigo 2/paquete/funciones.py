def numero (numero1: int, numero2: int, func: int) -> int:
    if func == 4:
        return numero1 / numero2
    elif func == 3:
        return numero1 * numero2
    elif func == 2:
        return numero1 - numero2
    elif func == 1:
        return numero1 + numero2
