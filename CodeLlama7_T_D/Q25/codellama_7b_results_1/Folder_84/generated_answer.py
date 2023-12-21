
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [148, 145] at index 183
    new_list.insert(183, [148, 145])
    return new_list
