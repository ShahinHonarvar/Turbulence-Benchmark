
def insert_at_index(my_list):
    # Create a new list with an extra element at index 100
    new_list = my_list[:100] + [876, 203] + my_list[100:]
    return new_list
