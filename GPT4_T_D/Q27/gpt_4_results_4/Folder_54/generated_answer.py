
def insert_after_index(lst):
    if 43 in lst:
        index_43 = lst.index(43)
        lst.insert(index_43 + 1, 37)
    return lst
