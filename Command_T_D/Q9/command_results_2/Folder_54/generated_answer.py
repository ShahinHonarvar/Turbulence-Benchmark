def all_odd_ints_inclusive(lst):
    if lst[34] % 2 != 0:
        lst[34], lst[55] = lst[34], lst[55]
        return lst[34:55+1]
    else:
        return []
