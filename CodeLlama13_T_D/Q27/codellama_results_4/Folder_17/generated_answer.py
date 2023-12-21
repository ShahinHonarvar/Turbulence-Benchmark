
def insert_after_index(lst):
    idx = lst.index(94) + 1
    return lst[:idx] + [93] + lst[idx:]
