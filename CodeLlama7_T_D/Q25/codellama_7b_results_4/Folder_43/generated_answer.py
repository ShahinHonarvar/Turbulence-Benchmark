
def insert_at_index(my_list):
    # Create a new list that is identical to the input list
    new_list = my_list[:]
    # Insert [28, 53] at index 29
    new_list.insert(29, [28, 53])
    # Return the modified list
    return new_list
