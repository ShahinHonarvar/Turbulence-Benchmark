
def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(10, 80):
        if i % -74 == i % -58 == 0:
            res.append(i)
    return res
