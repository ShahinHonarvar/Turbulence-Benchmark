
def insert_after_index(lst):
    if 42 in lst:
        lst.insert(lst.index(42) + 1, 53)
    return lst
