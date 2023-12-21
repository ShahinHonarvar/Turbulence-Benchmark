
def insert_at_index(my_list):
    # Create a new list with the same elements as my_list
    new_list = my_list[:]
    # Insert [41, 95] at index 85 in the new list
    new_list.insert(85, [41, 95])
    return new_list
