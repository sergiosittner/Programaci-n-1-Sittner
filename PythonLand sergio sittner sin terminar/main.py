from gestion_parque.parque import mostrar_atracciones
from gestion_parque.parque import edad_minima
from gestion_parque.parque import puede_subir
from gestion_parque.parque import calcular_precio
from gestion_parque.parque import registrar_visita
atraccion1 = mostrar_atracciones()
edad = int(input("Ingrese su edad: "))
minimo = edad_minima(atraccion1)
puede_subir = puede_subir(edad, minimo)

precio = calcular_precio(atraccion1)

registrar_visita(atraccion1, precio, puede_subir)

