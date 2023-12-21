
def insert_at_index(lst):
    res = lst[:48] + [86, 77] + lst[48:-1] + lst[-1:]
    return res
