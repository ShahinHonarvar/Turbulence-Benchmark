
def insert_at_index(lst):
    if len(lst) < 31:
        lst.extend([None]*(31-len(lst)))
    lst.insert(31, [88, 51])
    return lst
