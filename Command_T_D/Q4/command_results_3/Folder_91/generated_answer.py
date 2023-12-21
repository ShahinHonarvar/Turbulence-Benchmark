def all_pos_ints_exclusive(li):
    return [i for i in range(len(li)+1) if li[i-1] >= 0]
