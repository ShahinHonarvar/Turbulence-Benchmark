
def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[89]
    missing_nums = set(range(a + 1, b)) - set(nums[86:90])
    if not missing_nums:
        return ''
    s = sum(missing_nums)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]
