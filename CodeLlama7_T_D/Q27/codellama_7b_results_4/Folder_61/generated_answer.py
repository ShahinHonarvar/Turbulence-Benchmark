
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert 7 at the index immediately succeeding index 4
    new_list.insert(new_list.index(7) + 1, 7)
    return new_list
