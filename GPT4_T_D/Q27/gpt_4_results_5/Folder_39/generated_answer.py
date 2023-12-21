
def insert_after_index(lst):
    if 97 in lst:
        insert_index = lst.index(97) + 1
        lst.insert(insert_index, [47, 22])
    return lst
