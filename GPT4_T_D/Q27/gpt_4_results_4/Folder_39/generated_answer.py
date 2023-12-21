
def insert_after_index(lst):
    if 97 in lst:
        index= lst.index(97) + 1
        lst.insert(index, [47,22])
    return lst
