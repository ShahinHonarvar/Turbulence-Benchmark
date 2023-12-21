def all_ints_not_div_by_num(nums):
    return [i for i in range(10, 56) if i not in [x for x in nums if x % 36 == 0]]
