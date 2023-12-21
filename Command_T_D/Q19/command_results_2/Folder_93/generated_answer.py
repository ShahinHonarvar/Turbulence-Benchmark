def all_ints_not_div_by_num(nums):
    result = [nums[i] for i in range(33, 78) if not nums[i]%17]
    return result
