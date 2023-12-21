
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [80, 74] at index 60
    new_list.insert(60, [80, 74])
    return new_list
