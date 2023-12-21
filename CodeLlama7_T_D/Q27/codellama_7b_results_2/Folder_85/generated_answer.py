
def insert_after_index(my_list):
    # Create a new list with an extra element at index 52
    new_list = my_list[:51] + [304.62] + my_list[51:]
    return new_list
