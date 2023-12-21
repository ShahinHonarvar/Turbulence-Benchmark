
def all_ints_div_by_num(lst):
    if len(lst) < 2:
        return []
    else:
        return [i for i in lst[0:2] if i % 2 == 0]
