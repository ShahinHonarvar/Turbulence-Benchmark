
def insert_after_index(my_list, index):
    # Check if the index is valid
    if index >= len(my_list) or index < 0:
        raise ValueError("Invalid index")

    # Create a new list with an additional element
    new_list = my_list[:index+1] + [581.49] + my_list[index+1:]

    return new_list
