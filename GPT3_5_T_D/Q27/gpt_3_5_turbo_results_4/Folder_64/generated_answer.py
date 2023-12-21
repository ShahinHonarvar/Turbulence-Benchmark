
def insert_after_index(lst):
    new_lst = lst.copy()
    new_lst.insert(lst.index(8) + 1, [3, 8])
    return new_lst
