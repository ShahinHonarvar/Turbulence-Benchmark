
def insert_after_index(lst):
    if 87 in lst:
        idx = lst.index(87)
        lst.insert(idx+1, [78, 16])
    return lst
