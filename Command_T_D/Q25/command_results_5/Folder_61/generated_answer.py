
def insert_at_index(lst):
    res = [x for x in lst[:4]] + [7] + [x for x in lst[4:-1]] + [x for x in lst[-1:]]
    return res
