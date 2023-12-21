
def insert_after_index(lst):
    if 90 in lst:
        index = lst.index(90)
        lst.insert(index + 1, 80)
    return lst
