
def insert_after_index(lst):
    try:
        index_99 = lst.index(99)
        lst.insert(index_99 + 1, 99)
        return lst
    except ValueError:
        return lst
