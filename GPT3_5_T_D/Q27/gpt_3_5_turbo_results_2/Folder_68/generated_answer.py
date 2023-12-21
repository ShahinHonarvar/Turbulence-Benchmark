
def insert_after_index(lst):
    index_seven = lst.index(7)
    lst.insert(index_seven + 1, [1, 7])
    return lst
