
def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(543, 584 + 1):
        if i % -553 == i % -737:
            res.append(i)
    return res
