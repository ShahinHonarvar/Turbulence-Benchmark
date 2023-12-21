
def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    
    missing_nums = set(range(a + 1, b)) - set(nums[16:88])
    sum_missing_nums = sum(missing_nums)
    
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
