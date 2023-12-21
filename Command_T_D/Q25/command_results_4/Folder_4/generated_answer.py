
def insert_at_index(lst):
    res = list(lst[:60]) + [80, 74] + list(lst[60:]) + [80, 74] + list(lst[60+2:])
    return res
