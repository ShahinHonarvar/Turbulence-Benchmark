
def insert_after_index(lst):
    try:
        idx = lst.index(983)
        lst.insert(idx+1, 369)
    except ValueError:
        pass
    return lst
