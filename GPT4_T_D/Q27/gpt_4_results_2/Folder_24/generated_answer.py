
def insert_after_index(lst):
    if 42 in lst:
        index = lst.index(42)
        lst.insert(index + 1, 53)
    return lst
