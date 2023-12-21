
def insert_after_index(lst):
    new_lst = lst.copy()
    index = lst.index(38)
    new_lst.insert(index + 1, [27, 34])
    return new_lst
