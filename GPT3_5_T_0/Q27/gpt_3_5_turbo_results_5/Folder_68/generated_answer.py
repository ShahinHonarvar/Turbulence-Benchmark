
def insert_after_index(lst):
    index = lst.index(7)
    lst.insert(index + 1, [1, 7])
    return lst
