
def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(nums[29:54]))
    return '' if missing_nums_sum == 0 else (bin(missing_nums_sum)[2:] if missing_nums_sum % 2 != 0 else hex(missing_nums_sum)[2:])
