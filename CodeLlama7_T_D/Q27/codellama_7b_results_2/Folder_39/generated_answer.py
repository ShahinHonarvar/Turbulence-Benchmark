
def insert_after_index(my_list):
    # Create a new list with an extra element
    new_list = my_list[:97] + [47, 22] + my_list[97:]
    return new_list
