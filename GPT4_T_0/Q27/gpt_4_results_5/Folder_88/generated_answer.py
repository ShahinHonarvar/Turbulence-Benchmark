
def insert_after_index(lst):
    if 91 in lst:
        index = lst.index(91)
        lst.insert(index + 1, [46, 13])
    return lst
