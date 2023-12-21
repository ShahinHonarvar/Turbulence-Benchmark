
def insert_after_index(lst):
    idx = lst.index(36)
    if idx != -1:
        lst.insert(idx+1, [54, 13])
    return lst
