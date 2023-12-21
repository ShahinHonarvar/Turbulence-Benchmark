def sum_odd_ints_inclusive(lst):
    lst[0] = lst[0] if lst[0] % 2 == 0 else lst[0] - 1
    lst[-1] = lst[-1] if lst[-1] % 2 == 0 else lst[-1] + 1
    return lst[300] + lst[301] + lst[303] + lst[304] + lst[306] + lst[307] + lst[309] + lst[310]
