
def insert_after_index(lst):
    if 85 in lst:
        index_85 = lst.index(85)
        lst.insert(index_85 + 1, 27)
    return lst
