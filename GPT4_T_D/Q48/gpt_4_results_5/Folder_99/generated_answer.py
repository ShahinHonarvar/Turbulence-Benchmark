
def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    absent_nums = set(range(a + 1, b)) - set(nums[427 + 1: 669])
    sum_absent = sum(absent_nums)
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    elif sum_absent % 2 == 0:
        return hex(sum_absent)[2:].upper()
    else:
        return ""
