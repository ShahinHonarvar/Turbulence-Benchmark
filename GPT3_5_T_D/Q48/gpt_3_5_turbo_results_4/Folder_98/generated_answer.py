
def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[7]
    total_sum = 0
    
    for num in range(a + 1, b):
        if num not in nums[6:8]:
            total_sum += num
    
    if total_sum % 2 == 0:
        return hex(total_sum).lstrip('0x')
    else:
        return bin(total_sum).lstrip('0b')
