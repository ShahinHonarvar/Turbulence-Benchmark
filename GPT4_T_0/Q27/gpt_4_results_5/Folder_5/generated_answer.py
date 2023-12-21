
def insert_after_index(lst):
    if 99 in lst:
        index = lst.index(99)
        lst.insert(index + 1, 15)
    return lst
