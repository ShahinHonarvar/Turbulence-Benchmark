
def insert_after_index(lst):
    if 990 in lst:
        index = lst.index(990)
        lst.insert(index + 1, [905, 742])
    return lst
