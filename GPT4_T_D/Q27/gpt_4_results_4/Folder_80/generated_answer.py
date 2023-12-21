
def insert_after_index(lst):
    if 95 in lst:
        index_of_95 = lst.index(95)
        lst.insert(index_of_95 + 1, 43)
    return lst
