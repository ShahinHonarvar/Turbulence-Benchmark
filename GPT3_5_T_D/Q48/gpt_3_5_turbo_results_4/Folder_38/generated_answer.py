
def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[85]
    range_sum = sum(i for i in range(a + 1, b) if i not in nums[36:86])
    
    if range_sum % 2 == 0:
        return hex(range_sum)[2:]
    else:
        return bin(range_sum)[2:]
