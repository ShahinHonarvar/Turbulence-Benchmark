
def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[7]
    missing_nums_sum = sum([i for i in range(a + 1, b) if i not in nums[1:7]])
    
    if missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:].upper()
    else:
        return bin(missing_nums_sum)[2:]
