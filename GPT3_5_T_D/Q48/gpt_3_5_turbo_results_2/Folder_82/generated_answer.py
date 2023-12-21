
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[200]
    total = 0
    for num in range(a+1, b):
      if num not in nums[20:200]:
        total += num
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
