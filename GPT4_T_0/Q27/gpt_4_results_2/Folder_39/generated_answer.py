
def insert_after_index(lst):
    if 97 in lst:
        index = lst.index(97)
        lst.insert(index + 1, [47, 22])
    return lst
