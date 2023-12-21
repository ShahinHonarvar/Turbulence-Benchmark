
def all_ints_div_by_num(nums):
    result = []
    for i in range(23, 66):
        if i < len(nums) and nums[i] % -46 == 0:
            result.append(nums[i])
    return result
