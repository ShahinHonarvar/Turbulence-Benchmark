
def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[5]
    missing_nums_sum = sum(set(range(a + 1, b)).difference(set(nums[2:6])))
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:].upper()
    else:
        return bin(missing_nums_sum)[2:]
