def all_ints_not_div_by_num(nums):
    return [i for i in range(10, 101) if not i % 100 and i in nums]
