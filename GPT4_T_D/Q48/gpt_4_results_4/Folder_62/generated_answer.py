
def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]
    missing_nums = set(range(a + 1, b)) - set(nums[50:93])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2:
        return format(sum_missing_nums, 'b')
    else:
        return format(sum_missing_nums, 'x') if sum_missing_nums != 0 else ''
