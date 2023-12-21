
def return_binary_or_hexa(nums):
    a = nums[35]
    b = nums[64]
    missing_nums = set(range(a+1, b)) - set(nums[35:65])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ""
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
