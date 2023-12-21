
def insert_at_index(lst):
    if len(lst) < 28:
        lst.extend([None] * (28 - len(lst)))
    lst.insert(28, 20)
    return lst
