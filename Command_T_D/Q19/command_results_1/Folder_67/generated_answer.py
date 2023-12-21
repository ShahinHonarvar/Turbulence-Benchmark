def all_ints_not_div_by_num(nums):
    return [i for i in range(48, 92) if i not in set(nums) or not i % 90]
