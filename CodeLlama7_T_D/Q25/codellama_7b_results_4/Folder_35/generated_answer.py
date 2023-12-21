
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [876, 203] at index 100
    new_list.insert(100, [876, 203])
    return new_list
