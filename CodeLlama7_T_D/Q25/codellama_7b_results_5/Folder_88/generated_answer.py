
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [46, 13] at index 91
    new_list.insert(91, [46, 13])
    return new_list
