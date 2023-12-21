
def all_ints_not_div_by_num(nums):
    result = []
    for i in range(40, 57):
        if nums[i] % 84 != 0:
            result.append(nums[i])
    return result
