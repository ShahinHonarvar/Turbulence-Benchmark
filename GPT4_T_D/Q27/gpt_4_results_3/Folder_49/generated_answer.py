
def insert_after_index(lst):
    try:
        index_38 = lst.index(38)
        lst.insert(index_38 + 1, [27, 34])
    except ValueError:
        pass
    return lst
