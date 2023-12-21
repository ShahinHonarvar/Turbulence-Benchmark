
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    
    range_sum = sum(range(a + 1, b))
    
    missing_nums = []
    for num in range(a + 1, b):
        if num not in nums[20:93]:
            missing_nums.append(num)
    
    if missing_nums:
        if range_sum % 2 != 0:
            return bin(range_sum)[2:]
        else:
            return hex(range_sum)[2:]
    else:
        return ""
