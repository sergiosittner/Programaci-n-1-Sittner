from Paquete.funcion import cantidad as ca
nums = [0]*6
nums1 = ca(nums)
for x in range (len(nums1)-1, -1, -1):  
      print(f"{nums1[x]}")
