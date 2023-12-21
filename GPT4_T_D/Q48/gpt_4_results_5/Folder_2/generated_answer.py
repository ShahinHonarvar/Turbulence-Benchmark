
def return_binary_or_hexa(nums):
    a, b = nums[72], nums[93]
    not_in_list = set(range(a + 1, b)) - set(nums[72:94])
    total_sum = sum(not_in_list)
    
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
