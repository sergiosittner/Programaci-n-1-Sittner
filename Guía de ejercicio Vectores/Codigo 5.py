from Paquete.funcion import cantidad as ca
nums = [0]*10
ca(nums)
asignado = int(input("ingrese un numero : ")) 
encontrado = 0
for x in range (len(nums)):    
    if nums[x] == asignado: 
       encontrado = True
       break


if encontrado == True:
    print(f"Su numero esta en el array y su posicion es {x}")

else:
    print("Su numero no esta en el array")
