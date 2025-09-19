from Paquete.funcion import cantidad as ca
nums = [0]*10
ca(nums)
suma = 0
for x in range(len(nums)):
    suma += nums[x]
    
print(suma)