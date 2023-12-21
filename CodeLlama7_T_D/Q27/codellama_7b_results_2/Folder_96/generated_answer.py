
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [51, 29] at the index immediately succeeding index 74
    new_list.insert(new_list.index(74) + 1, [51, 29])
    return new_list
