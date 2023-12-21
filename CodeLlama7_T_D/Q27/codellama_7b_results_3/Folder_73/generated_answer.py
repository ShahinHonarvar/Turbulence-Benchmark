
def insert_after_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Find the index of the element after which we want to insert the new value
    next_index = my_list.index(637.22) + 1
    # Insert the new value at the appropriate index in the new list
    new_list.insert(next_index, 637.22)
    return new_list
