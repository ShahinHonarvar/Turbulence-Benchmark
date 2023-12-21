
def insert_at_index(my_list):
    # Create a new list with an extra element at index 38
    new_list = my_list[:38] + [27, 34] + my_list[38:]
    return new_list
