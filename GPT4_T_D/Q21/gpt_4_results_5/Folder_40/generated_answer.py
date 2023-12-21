
def all_ints_div_by_num(lst):
    try:
        return [lst[0]] if lst[0] % 2 == 0 else []
    except IndexError:
        return []
