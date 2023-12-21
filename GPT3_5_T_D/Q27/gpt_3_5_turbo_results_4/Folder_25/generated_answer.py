
def insert_after_index(lst):
    new_lst = lst.copy()
    new_lst.insert(lst.index(30) + 1, 37)
    return new_lst
