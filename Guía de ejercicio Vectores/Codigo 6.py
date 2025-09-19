from Paquete.funcion import cantidad as ca
nums = [0]*7
ca(nums)
maximo = nums[0]
posicion = 0
encontrado = 0
for x in nums:    
    if x > maximo: 
       maximo = x
       encontrado = posicion
    posicion +=1

print(f"El valor mas alto del array es {maximo} y encuentra en {encontrado+1}")

