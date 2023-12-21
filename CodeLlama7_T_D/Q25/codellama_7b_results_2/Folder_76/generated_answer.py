
def insert_at_index(my_list):
    # Create a new list with an extra element at index 166
    new_list = my_list[:165] + [232] + my_list[165:]
    return new_list
