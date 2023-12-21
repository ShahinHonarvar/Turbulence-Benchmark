
def insert_after_index(lst):
    if 20 in lst:
        index = lst.index(20) + 1
        lst.insert(index, 80)
        return lst
    else:
        return lst
