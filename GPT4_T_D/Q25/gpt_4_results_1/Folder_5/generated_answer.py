
def insert_at_index(lst):
    if len(lst) <= 99:
        lst.extend([15]*(100-len(lst)))
    else:
        lst.insert(99, 15)
    return lst
