
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [15, 51] at the index immediately succeeding index 76
    new_list.insert(new_list.index(76) + 1, [15, 51])
    return new_list
