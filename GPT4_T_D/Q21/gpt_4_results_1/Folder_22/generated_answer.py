
def all_ints_div_by_num(lst):
    try:
        return [x for x in lst[10:11] if x % 1 == 0]
    except IndexError:
        return []
