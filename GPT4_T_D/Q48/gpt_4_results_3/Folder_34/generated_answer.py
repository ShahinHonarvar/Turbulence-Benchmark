
def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    sum_nums = sum(set(range(a + 1, b)) - set(nums[60:201]))

    if sum_nums == 0:
        return ""
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:].upper()
    else:
        return bin(sum_nums)[2:]
