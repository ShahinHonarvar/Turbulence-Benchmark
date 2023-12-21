
def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[98]
    missing_nums = set(range(a + 1, b)) - set(nums[70:99])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return bin(sum_missing_nums)[2:]
