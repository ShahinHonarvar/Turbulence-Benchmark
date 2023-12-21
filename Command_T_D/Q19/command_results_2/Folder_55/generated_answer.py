def all_ints_not_div_by_num(nums):
    return [i for i in range(0, 10) if i not in [j for j in range(0, 10) if j % 10 == 0]]
