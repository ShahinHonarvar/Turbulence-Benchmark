
def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[43]
    missing_nums_sum = sum(set(range(a+1, b)) - set(nums[20:44]))
    if missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:]
    else:
        return bin(missing_nums_sum)[2:]
