
def insert_after_index(original_list):
    index_value = original_list.index(38)
    original_list.insert(index_value+1, [27, 34])
    return original_list
