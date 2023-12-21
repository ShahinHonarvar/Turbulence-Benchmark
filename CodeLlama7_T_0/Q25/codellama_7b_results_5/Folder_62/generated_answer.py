
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [90, 76] at index 35
    new_list.insert(35, [90, 76])
    return new_list
