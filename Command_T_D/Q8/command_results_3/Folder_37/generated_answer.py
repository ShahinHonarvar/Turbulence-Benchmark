def all_even_ints_exclusive(lst):
    return [x for x in range(1,len(lst)-1) if lst[x] % 2 == 0]
