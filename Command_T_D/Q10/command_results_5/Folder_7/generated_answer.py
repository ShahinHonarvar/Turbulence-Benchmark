def all_odd_ints_exclusive(lst):
    if lst[322]&1==0:
        return []
    return [x for x in range(323, 972, 2) if lst[x]&1==1]
