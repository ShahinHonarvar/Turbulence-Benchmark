
def all_ints_not_div_by_num(lst):
    res = []
    for num in lst[9:10]:
        if num % 8 != 0:
            res.append(num)
    return res
