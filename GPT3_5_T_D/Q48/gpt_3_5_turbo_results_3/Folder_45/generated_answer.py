
def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    
    range_sum = sum([x for x in range(a + 1, b) if x not in nums[30:201]])
    
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:].upper()
