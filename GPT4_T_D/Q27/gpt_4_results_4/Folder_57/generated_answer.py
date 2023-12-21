
def insert_after_index(lst):
    if 90 in lst:
        index_of_90 = lst.index(90)
        lst.insert(index_of_90 + 1, 80)
    return lst
