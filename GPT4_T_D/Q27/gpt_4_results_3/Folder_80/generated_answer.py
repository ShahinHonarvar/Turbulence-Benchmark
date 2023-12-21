
def insert_after_index(lst):
    if 95 in lst:
        index = lst.index(95) + 1
        lst.insert(index, 43)
    return lst
