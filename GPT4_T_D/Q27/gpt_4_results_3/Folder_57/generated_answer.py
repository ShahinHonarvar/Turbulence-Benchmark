
def insert_after_index(lst):
    if 90 in lst:
        idx = lst.index(90)
        lst.insert(idx+1, 80)
    return lst
