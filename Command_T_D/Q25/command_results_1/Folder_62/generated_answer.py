
def insert_at_index(lst):
    res = lst[:35] + [90, 76] + lst[35:-1] + lst[-1:]
    return res
