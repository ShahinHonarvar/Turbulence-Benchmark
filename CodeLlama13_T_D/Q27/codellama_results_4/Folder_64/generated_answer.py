
def insert_after_index(lst):
    idx = lst.index(8) + 1
    return lst[:idx] + [3, 8] + lst[idx:]
