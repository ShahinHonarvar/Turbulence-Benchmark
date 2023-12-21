
def find_second_largest_num(lst):
    return lst[43:86][-2] if lst[43:86].count(lst[43:86][-1]) == 1 else None
