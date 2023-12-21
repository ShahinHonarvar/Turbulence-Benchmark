def all_odd_ints_exclusive(lst):
    if lst[59] % 2 == 1:
        if lst[93] % 2 == 1:
            return lst[59:93]
        else:
            return lst[59:]
    else:
        return []
