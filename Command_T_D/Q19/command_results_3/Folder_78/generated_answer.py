def all_ints_not_div_by_num(nums):
    return [i for i in range(10, 56) if not i % 36 and i in nums]
