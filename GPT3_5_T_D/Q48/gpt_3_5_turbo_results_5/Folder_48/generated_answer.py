
def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    total_sum = sum(range(a + 1, b))
    missing_nums = [i for i in range(a + 1, b) if i not in nums[933:997]]
    
    if len(missing_nums) == 0:
        return ""
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    
    return hex(total_sum)[2:]
