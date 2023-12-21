
def insert_after_index(lst):
    if 93 in lst:
        index_value = lst.index(93)
        lst.insert(index_value+1, [33, 78])
    return lst
