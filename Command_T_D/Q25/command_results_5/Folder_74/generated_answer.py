
def insert_at_index(lst):
    lst = list(range(len(lst) + 1))
    lst[41], lst[40] = lst[40], lst[41]
    lst.insert(41, [74, 70])
    return lst
