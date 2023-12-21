def all_ints_not_div_by_num(nums):
    result = [i for i in range(0, 9) if not (nums[i] % 3 == 0)]
    return result
