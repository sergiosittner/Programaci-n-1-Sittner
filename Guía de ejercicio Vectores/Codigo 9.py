from Paquete.funcion import cantidad as ca
nums = [0]*10
ca(nums)
for x in range (len(nums)):  
      if (nums[x]%2) == 0:
            nums[x] = 0

for x in range (len(nums)):
      print(nums[x])
