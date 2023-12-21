
def insert_after_index(lst):
    try:
        index = lst.index(44)
        lst.insert(index + 1, [40, 27])
    except ValueError:
        return lst
    return lst
