
def insert_after_index(lst):
    result = lst[:]
    result.insert(lst.index(42) + 1, 53)
    return result
