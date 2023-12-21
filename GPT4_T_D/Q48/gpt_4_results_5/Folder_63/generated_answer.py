
def return_binary_or_hexa(nums):
    a = nums[81]
    b = nums[86]
    missing_nums = set(range(a + 1, b)) - set(nums[81:87])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')
