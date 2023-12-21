
def insert_after_index(lst):
    index_of_99 = lst.index(99)
    lst.insert(index_of_99 + 1, 99)
    return lst
