
def insert_at_index(my_list):
    # Create a new list with an extra element at index 66
    new_list = my_list[:66] + [45] + my_list[66:]
    return new_list
