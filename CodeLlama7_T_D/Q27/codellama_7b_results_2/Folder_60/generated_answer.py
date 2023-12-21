
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Find the index of the element that we want to insert after
    target_index = my_list.index(74) + 1
    # Insert the element at the target index
    new_list.insert(target_index, 74)
    return new_list
