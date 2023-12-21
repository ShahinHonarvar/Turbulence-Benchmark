
def all_ints_not_div_by_num(lst):
    if len(lst) < 3:
        return []
    else:
        result = [i for i in lst[2:] if i % lst[0] != 0]
        return result
