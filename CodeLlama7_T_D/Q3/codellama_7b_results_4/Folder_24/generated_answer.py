
def all_pos_ints_inclusive(my_list):
    # Find the starting index of the positive integers
    start_index = next((i for i, x in enumerate(my_list) if x > 0), None)
    # If no positive integers exist in the list, return an empty list
    if start_index is None:
        return []

    # Find the ending index of the positive integers

    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x <= 0), None)
    # If no positive integers exist beyond the starting index, return an empty list
    if end_index is None:
        return []

    # Return the list of all positive integers from the specified range
    return my_list[start_index:end_index]
