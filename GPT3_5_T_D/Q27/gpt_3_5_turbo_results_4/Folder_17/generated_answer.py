
def insert_after_index(lst):
    new_lst = lst[:]
    new_lst.insert(lst.index(94)+1, 93)
    return new_lst
