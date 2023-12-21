
def insert_after_index(lst):
    idx = lst.index(99) + 1
    return lst[:idx] + [99] + lst[idx:]
