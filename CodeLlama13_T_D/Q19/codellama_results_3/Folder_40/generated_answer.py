
def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 1 != 0:
            result.append(nums[i])
    return result
