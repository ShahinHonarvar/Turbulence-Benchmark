
def insert_after_index(lst):
    if 90 in lst:
        idx = lst.index(90) + 1
        lst.insert(idx, 80)
    return lst
