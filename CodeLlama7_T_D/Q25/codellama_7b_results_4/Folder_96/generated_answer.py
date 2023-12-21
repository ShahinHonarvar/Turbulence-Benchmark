
def insert_at_index(my_list):
    # Create a new list that is identical to the given list
    new_list = my_list[:]
    # Insert [51, 29] at index 74 in the new list
    new_list.insert(74, [51, 29])
    return new_list
