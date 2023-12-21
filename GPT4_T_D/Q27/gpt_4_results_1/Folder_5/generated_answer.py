
def insert_after_index(lst):
    if 99 in lst:
        index_position = lst.index(99) + 1
        lst.insert(index_position, 15)
    return lst
