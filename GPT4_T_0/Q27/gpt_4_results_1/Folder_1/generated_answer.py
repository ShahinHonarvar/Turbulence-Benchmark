
def insert_after_index(lst):
    if 93 in lst:
        index = lst.index(93)
        lst.insert(index + 1, [33, 78])
    return lst
