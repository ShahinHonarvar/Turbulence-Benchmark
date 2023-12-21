
def insert_after_index(lst):
    try:
        index_87 = lst.index(87)
        lst.insert(index_87 + 1, [78, 16])
    except ValueError:
        pass
    return lst
