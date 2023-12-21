
def insert_after_index(my_list):
    new_list = my_list[:]
    # Insert [41, 95] at the index immediately succeeding index 85
    new_list.insert(new_list.index(85) + 1, [41, 95])
    return new_list
