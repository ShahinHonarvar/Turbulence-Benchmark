
def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    
    valid_nums = set(nums[78:84]) - set(nums[78])
    
    total_sum = sum(num for num in range(a + 1, b) if num not in valid_nums)
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
