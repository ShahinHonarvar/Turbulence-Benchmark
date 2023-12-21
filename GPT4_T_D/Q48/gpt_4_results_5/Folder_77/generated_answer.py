
def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    missing_nums = list(set(range(a + 1, b)) - set(nums[18:53]))
    total = sum(missing_nums)
    if not missing_nums:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
