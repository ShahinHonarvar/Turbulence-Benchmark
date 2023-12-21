
def insert_at_index(lst):
    if len(lst) >= 97:
        lst.insert(97, [47, 22])
    else:
        lst.append([47, 22])
    return lst
