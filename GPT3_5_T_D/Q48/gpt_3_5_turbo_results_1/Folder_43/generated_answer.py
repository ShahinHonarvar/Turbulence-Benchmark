
def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[28]
    range_nums = set(nums[10:29])
    sum_nums = sum(x for x in range(a+1, b) if x not in range_nums)
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
