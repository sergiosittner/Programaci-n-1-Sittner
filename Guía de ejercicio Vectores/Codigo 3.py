from Paquete.funcionfloat import cantidad as ca
nums = [0]*6
ca(nums)
suma = 0
for x in range(len(nums)):
    suma += nums[x]

div = (suma / len(nums))
print(div)  
