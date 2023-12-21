
def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    missing_nums_sum = sum(set(range(a+1, b)) - set(nums[16:87]))
    if missing_nums_sum == 0:
        return ""
    elif missing_nums_sum % 2:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
