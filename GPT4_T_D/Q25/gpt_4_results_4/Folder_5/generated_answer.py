
def insert_at_index(lst):
    if len(lst) >= 99:
        lst.insert(99, 15)
    else:
        lst.append(15)
    return lst
