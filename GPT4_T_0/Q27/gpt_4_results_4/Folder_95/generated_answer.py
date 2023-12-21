
def insert_after_index(lst):
    if 20 in lst:
        index = lst.index(20)
        lst.insert(index + 1, 80)
    return lst
