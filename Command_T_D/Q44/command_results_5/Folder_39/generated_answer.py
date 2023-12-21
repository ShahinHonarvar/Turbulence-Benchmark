import set
def composite_nums_between_indices(list):
    idx_62 = list.index(62) + 1
    idx_92 = list.index(92) + 1
    return set(list[idx_62:idx_92])
