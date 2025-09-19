from Paquete.funcion import cantidad as ca
nums = [0]*6
ca(nums)
numero = int(input("Ingrese el numero a buscar: "))
encontrado = 0
for x in range (len(nums)):  
      if (nums[x]) == numero:
            print(f"El numero está en la pocisión {x+1}")
            encontrado = True
            break

if not encontrado:
      print ("-1")
            
      

