
def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[88]
    total_sum = sum(nums[a + 1:b])
    missing_nums = [num for num in range(a + 1, b) if num not in nums]
    
    if len(missing_nums) == 0:
        return ""
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
