from Paquete.funcion import cantidad as ca
nums = [0]*8
ca(nums)
contador = 0 
for x in nums:
    if x > 100:
        contador += 1

print(contador)