
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[3]
    missing_nums = set(range(a + 1, b)) - set(nums[1:3])
    if not missing_nums:
        return ""
    sum_nums = sum(missing_nums)
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]
