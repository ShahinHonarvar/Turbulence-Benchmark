
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [83, 14] at index 21
    new_list.insert(21, [83, 14])
    return new_list
