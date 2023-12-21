
def insert_at_index(my_list):
    # Create a new list with the original elements and the inserted element at index 8
    new_list = my_list[:8] + [3, 8] + my_list[8:]
    return new_list
