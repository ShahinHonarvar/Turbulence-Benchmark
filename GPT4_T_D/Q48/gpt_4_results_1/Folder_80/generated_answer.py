
def return_binary_or_hexa(nums):
    a = nums[57] + 1
    b = nums[84] - 1
    missing_numbers = set(range(a, b + 1)) - set(nums[57:85])
    total_sum = sum(missing_numbers)
    if total_sum == 0: 
        return ''
    elif total_sum % 2 == 1: 
        return bin(total_sum)[2:]
    else: 
        return hex(total_sum)[2:].upper()
