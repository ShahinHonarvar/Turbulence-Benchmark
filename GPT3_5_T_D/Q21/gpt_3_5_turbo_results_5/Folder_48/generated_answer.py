
def all_ints_div_by_num(nums):
    result = []
    for i in range(574, 745):
        if i < len(nums) and nums[i] % 649 == 0:
            result.append(nums[i])
    return result
