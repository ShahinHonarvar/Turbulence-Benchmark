
def insert_after_index(my_list, index):
    # Check if the index is valid
    if index < 0 or index >= len(my_list):
        raise ValueError("Invalid index")

    # Create a new list with the element inserted at the specified index
    new_list = my_list[:index+1] + [581.49] + my_list[index+1:]

    return new_list
