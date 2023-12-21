
def insert_at_index(lst):
    res = lst[:43] + [37] + lst[43:-1] + lst[-1:]
    return res
