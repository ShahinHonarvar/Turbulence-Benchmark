
def insert_after_index(lst):
    try:
        index = lst.index(564)
        lst.insert(index + 1, 149)
    except ValueError:
        pass
    return lst
