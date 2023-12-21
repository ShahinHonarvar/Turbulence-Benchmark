
def return_binary_or_hexa(nums):
    a = nums[55]
    b = nums[84]
    
    sum_total = sum(set(range(a + 1, b)) - set(nums[55:85]))
    
    if sum_total % 2 != 0:
        return bin(sum_total)[2:]
    elif sum_total % 2 == 0 and sum_total != 0:
        return hex(sum_total)[2:].upper()
    else:
        return ""
