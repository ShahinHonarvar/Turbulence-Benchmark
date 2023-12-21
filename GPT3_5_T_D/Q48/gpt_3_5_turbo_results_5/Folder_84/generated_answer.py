
def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    total = sum(nums[a+1:b])
    
    not_present = [x for x in range(a+1, b) if x not in nums[32:44]]
    
    if len(not_present) == 0:
        return ""
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
