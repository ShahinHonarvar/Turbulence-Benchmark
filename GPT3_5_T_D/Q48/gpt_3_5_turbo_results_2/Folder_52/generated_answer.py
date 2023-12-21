
def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[81]

    missing_nums = set(range(a + 1, b)) - set(nums[39:81])

    if len(missing_nums) == 0:
        return ""

    sum_missing_nums = sum(missing_nums)

    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]
