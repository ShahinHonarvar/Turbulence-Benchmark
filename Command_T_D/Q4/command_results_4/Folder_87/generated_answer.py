def all_pos_ints_exclusive(a):
    b = [int(i) for i in range(32, 100)]
    return [i for i in b if i in a]
