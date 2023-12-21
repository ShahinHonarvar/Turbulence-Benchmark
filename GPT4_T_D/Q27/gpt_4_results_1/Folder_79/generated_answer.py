
def insert_after_index(lst):
    index = 28
    to_insert = [41, 69]
    if len(lst) >= 28:
        lst.insert(index + 1, to_insert)
    return lst
