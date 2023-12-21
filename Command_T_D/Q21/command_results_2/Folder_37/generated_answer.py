def all_ints_div_by_num(lst):
    return [i for i in range(4, len(lst) + 1, 3) if lst[i] % 3 == 0]
