
def insert_after_index(lst):
    try:
        index_35 = lst.index(35)
        lst.insert(index_35 + 1, [90, 76])
    except ValueError:
        pass
    return lst
