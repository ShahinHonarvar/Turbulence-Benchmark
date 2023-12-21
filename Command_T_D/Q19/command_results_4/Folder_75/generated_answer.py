def all_ints_not_div_by_num(nums):
    return [i for i in range(20, 52) if not i % -48 and i in nums]
