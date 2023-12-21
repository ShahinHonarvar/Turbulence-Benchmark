
def insert_after_index(lst):
    new_lst = list(lst)
    index = new_lst.index(96)
    new_lst.insert(index + 1, 36)
    return new_lst
