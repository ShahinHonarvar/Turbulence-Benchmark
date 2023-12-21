
def insert_after_index(lst):
    idx = lst.index(693) + 1
    return lst[:idx] + [606, 873] + lst[idx:]
