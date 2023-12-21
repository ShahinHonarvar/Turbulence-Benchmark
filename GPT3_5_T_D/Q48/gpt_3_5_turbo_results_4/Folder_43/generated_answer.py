
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[28]
    
    total_sum = sum([num for num in range(a+1, b) if num not in nums[10:29]])
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
