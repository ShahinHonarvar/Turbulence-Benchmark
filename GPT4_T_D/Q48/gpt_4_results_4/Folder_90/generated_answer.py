
def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    sum_nums = sum(set(range(a + 1, b)) - set(nums[61:90]))
    if sum_nums % 2 != 0:
        return bin(sum_nums)[2:]
    elif sum_nums != 0:
        return hex(sum_nums)[2:].upper()
    else:
        return ""
