
def insert_after_index(lst):
    if 63 in lst:
        lst.insert(lst.index(63) + 1, 99)
    return lst
