
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[4]
    total = sum(nums[a+1:b])
    missing_nums = [x for x in range(a+1, b) if x not in nums]
    
    if len(missing_nums) == 0:
        return ""
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
