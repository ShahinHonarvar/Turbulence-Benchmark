
def return_binary_or_hexa(nums):
    a, b = nums[40], nums[200]
    lst = nums[a + 1 : b - 1]
    if lst:
        return ''
    else:
        return '0b' + '0' * (a + 1) + '1' * (b - a - 1) or '0x' + '0' * (a + 1) + '1' * (b - a - 1)
