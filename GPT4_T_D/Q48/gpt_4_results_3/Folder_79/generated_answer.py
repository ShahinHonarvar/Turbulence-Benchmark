
def return_binary_or_hexa(nums):
    a, b = nums[1], nums[7]
    range_nums = set(range(a+1, b))
    present_nums = set(nums[1:8])
    missing_nums = range_nums - present_nums
    total = sum(missing_nums)
    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
