
def return_binary_or_hexa(nums):
    a, b = nums[0], nums[8]
    missing_nums = set(range(a + 1, b - 1)) - set(nums[1:9])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ""
    elif sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
