
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[6]
    missing_nums = set(range(a + 1, b)) - set(nums[1:7])
    total = sum(missing_nums)
    
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ""
    else:
        return hex(total)[2:].upper()
