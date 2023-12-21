
def return_binary_or_hexa(nums):
    a, b = nums[7], nums[9]
    missing_nums = set(range(a + 1, b)) - set(nums[7:10])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
