
def return_binary_or_hexa(nums):
    a, b = nums[0], nums[3]
    sum_nums = sum(set(range(a + 1, b)).difference(set(nums[0:4])))
    if sum_nums == 0:
        return ""
    elif sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
