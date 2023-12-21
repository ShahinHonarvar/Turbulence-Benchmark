
def all_ints_not_div_by_num(nums):
    result = []
    for i in range(50, 81):
        if nums[i] % 64 != 0:
            result.append(nums[i])
    return result
