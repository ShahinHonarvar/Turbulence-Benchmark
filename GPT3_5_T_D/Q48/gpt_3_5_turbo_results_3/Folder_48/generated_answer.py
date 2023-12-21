
def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    
    total = sum(nums[a+1:b])
    
    missing_nums = [i for i in range(a+1, b) if i not in nums[a+1:b]]
    
    if len(missing_nums) == 0:
        return ""
    
    if total % 2 == 1:
        return bin(total)[2:]
    
    return hex(total)[2:].upper()
