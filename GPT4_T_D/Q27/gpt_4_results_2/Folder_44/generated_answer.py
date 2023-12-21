
def insert_after_index(lst):
    index_position = 48
    item_to_insert = [86, 77]
    if index_position < len(lst):
        lst.insert(index_position + 1, item_to_insert)
    return lst
