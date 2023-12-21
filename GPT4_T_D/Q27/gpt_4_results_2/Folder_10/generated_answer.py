
def insert_after_index(lst):
    idx = lst.index(56) if 56 in lst else -1
    if idx != -1:
        lst.insert(idx+1, 54)
    return lst
