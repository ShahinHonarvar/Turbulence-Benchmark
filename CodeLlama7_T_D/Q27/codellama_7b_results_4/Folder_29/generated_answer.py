
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Find the index of the element that we want to insert after
    index_to_insert_after = my_list.index(36) - 1
    # Insert 36 at the index immediately succeeding index 96
    new_list.insert(index_to_insert_after + 1, 36)
    return new_list
