
def insert_after_index(lst):
    i = lst.index(57) + 1
    return lst[:i] + [96] + lst[i:]
