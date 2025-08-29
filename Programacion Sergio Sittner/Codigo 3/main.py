from paquete.calculo import area_triangulo as tri
base = float(input("ingrese la base del triangulo: "))
altura = float(input("ingrese la altura del triangulo: "))
area = tri(base, altura)
print(f"el area del triangulo es {area}")
