def all_ints_not_div_by_num(nums):
    lst = [i for i in range(80, 200) if not i % 1000]
    return [x for x in nums if x in lst]
