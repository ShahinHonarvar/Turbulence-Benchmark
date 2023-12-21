
def insert_after_index(lst):
    if 62 not in lst:
        return lst
    else:
        index = lst.index(62)
        lst.insert(index + 1, [19, 13])
        return lst
