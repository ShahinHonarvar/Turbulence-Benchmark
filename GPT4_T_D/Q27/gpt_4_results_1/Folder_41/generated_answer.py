
def insert_after_index(lst):
    if 87 in lst:
        idx_of_87 = lst.index(87)
        lst.insert(idx_of_87+1, [78, 16])
    return lst
