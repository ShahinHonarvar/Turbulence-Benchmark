
def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    missing_nums = set(range(a + 1, b)) - set(nums[29:54])
    total_sum = sum(missing_nums)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')
