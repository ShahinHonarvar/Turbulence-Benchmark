
def insert_at_index(lst):
    if len(lst) >= 99:
        lst.insert(99, 99)
    else:
        lst.extend([0]*(99-len(lst)))
        lst.append(99)
    return lst
