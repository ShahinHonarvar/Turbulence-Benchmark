
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[88]
    
    total_sum = 0
    missing_nums = []
    for num in range(a + 1, b):
        if num not in nums[56:88]:
            total_sum += num
        else:
            missing_nums.append(num)
            
    if len(missing_nums) == 0:
        return ""
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
