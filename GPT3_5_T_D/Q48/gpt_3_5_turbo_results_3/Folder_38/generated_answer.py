
def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[85]
    
    total_sum = 0
    for num in range(a+1, b):
        if num not in nums[36:86]:
            total_sum += num
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
