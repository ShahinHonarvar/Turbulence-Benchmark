
def insert_after_index(lst):
    try:
        idx = lst.index(93)
        lst.insert(idx + 1, [33, 78])
    except ValueError:
        pass
    return lst
