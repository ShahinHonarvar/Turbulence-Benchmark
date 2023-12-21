def all_ints_div_by_num(nums):
    result = [i for i in range(0, len(nums)) if nums[i] % 9 == 0]
    return result
