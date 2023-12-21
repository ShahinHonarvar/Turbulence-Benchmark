
def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    nums_range = set(range(a + 1, b))
    nums_set = set(nums[37:54])
    diff_set = nums_range - nums_set
    if len(diff_set) == 0:
        return ""
    sum_nums = sum(diff_set)
    if sum_nums % 2 == 1:
        return format(sum_nums, 'b')
    else:
        return format(sum_nums, 'x')
