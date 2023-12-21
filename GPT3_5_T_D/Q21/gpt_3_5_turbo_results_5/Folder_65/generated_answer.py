
def all_ints_div_by_num(nums):
    result = []
    for i in range(14, 57):
        if nums[i] % -59 == 0:
            result.append(nums[i])
    return result
