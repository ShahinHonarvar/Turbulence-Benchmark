
def insert_after_index(lst):
    idx = lst.index(370) + 1
    return lst[:idx] + [285.4] + lst[idx:]
