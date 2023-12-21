
def all_ints_div_by_num(lst):
    res = []
    if len(lst) > 10:
        for num in lst[10:11]:
            if num % 1 == 0:
                res.append(num)
    return res
