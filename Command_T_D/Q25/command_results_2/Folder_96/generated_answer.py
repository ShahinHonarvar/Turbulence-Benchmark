
def insert_at_index(lst):
    res = lst[:74] + [51, 29] + lst[74:-1] + lst[-1:]
    return res
