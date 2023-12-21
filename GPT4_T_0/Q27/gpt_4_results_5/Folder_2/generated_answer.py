
def insert_after_index(lst):
    if 427 in lst:
        index = lst.index(427)
        lst.insert(index + 1, [312, 441])
    return lst
