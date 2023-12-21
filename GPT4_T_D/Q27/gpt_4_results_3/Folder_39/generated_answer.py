
def insert_after_index(lst):
    try:
        idx = lst.index(97)
        lst.insert(idx+1, [47, 22])
    except ValueError:
        pass

    return lst
