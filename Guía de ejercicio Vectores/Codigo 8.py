from Paquete.funcion import cantidad as ca
nums = [0]*5
ca(nums)
nums1 = [0]*5
ca(nums1)
for x in range (len(nums)):  
      if nums[x] == nums1[x]:
            print(f"en la pocisión {x+1} son iguales")
      else:
            print(f"en la pocisión {x+1} son diferentes")
