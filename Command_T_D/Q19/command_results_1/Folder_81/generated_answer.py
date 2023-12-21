def all_ints_not_div_by_num(nums):
    return [i for i in range(10, 101) if i not in nums and not (i % 100 == 0)]
