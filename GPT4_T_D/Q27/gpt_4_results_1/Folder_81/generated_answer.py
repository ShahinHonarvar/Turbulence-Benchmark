
def insert_after_index(lst):
    try:
        index = lst.index(28)
        lst.insert(index + 1, 20)
    except ValueError:
        pass
    return lst
