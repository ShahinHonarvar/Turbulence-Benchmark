
def insert_after_index(lst):
    if 62 in lst:
        index_62 = lst.index(62)
        lst.insert(index_62+1, 51)
    return lst
