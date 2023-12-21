
def insert_after_index(lst):
    new_lst = lst.copy()
    index = new_lst.index(66)
    new_lst.insert(index + 1, 45)
    return new_lst
