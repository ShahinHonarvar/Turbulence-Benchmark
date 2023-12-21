
def insert_after_index(lst):
    new_list = lst.copy()
    new_list.insert(lst.index(89) + 1, 86)
    return new_list
