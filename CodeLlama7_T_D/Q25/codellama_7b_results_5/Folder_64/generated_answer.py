
def insert_at_index(my_list, index):
    # Check if the given list and index are valid
    if not isinstance(my_list, list) or not isinstance(index, int):
        raise TypeError("The given list and index must be of type list and int respectively")
    
    # Insert [3, 8] at index 8 in the given list
    my_list.insert(index, [3, 8])
    return my_list
