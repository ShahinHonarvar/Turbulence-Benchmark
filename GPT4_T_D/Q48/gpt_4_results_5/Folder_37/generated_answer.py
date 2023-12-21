
def return_binary_or_hexa(nums):
    a, b = nums[min(2, len(nums)-1)], nums[min(7, len(nums)-1)]
    missing_nums = set(range(a + 1, b)) - set(nums[2:min(7, len(nums))])
    summed = sum(missing_nums)
    if summed == 0:
        return ''
    return format(summed, 'b') if summed%2 else format(summed, 'x')
