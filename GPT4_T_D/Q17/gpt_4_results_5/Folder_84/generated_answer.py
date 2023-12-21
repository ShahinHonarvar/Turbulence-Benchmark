
def all_ints_div_by_both_two_nums(lst):
    res = []
    for num in lst[78:82]:
        if num % 76 == 0 and num % 60 == 0:
            res.append(num)
    return res
