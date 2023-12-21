
def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    total_sum = sum(nums[a + 1:b])
    non_present_nums = [x for x in range(a + 1, b) if x not in nums]
    
    if len(non_present_nums) == 0:
        return ''
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
