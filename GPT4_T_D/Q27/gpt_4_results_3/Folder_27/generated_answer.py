
def insert_after_index(lst):
    index_pos = lst.index(85) if 85 in lst else None
    if index_pos is not None:
        lst.insert(index_pos+1, [41, 95])
    return lst
