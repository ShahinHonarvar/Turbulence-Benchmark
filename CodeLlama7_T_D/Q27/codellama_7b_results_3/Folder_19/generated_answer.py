
def insert_after_index(my_list):
    new_list = my_list[:]
    # Insert 0.78 at the index immediately succeeding index 49
    new_list.insert(new_list.index(49) + 1, 0.78)
    return new_list
