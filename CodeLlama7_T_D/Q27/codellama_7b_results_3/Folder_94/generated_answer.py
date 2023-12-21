
def insert_after_index(my_list):
    # Find the index of the element to insert after
    try:
        insert_after_idx = my_list.index(517.71) + 1
    except ValueError:
        # If the element is not found, return the original list
        return my_list

    # Create a new list with the inserted element
    new_list = my_list[:insert_after_idx] + [517.71] + my_list[insert_after_idx:]

    # Return the new list
    return new_list
