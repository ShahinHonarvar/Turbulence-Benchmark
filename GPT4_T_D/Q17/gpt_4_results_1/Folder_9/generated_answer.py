
def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(70, 201 if len(lst) > 200 else len(lst)):
        if lst[i] % 3 == 0 and lst[i] % -300 == 0:
            res.append(lst[i])
    return res
