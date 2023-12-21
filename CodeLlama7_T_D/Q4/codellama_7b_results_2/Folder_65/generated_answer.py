
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the range
    start_index = next((i for i, x in enumerate(my_list) if x > 0), None)
    # If no positive integers exist in the range, return an empty list
    if start_index is None:
        return []

    # Find the last positive integer in the range

    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x > 0), None)
    # If no positive integers exist in the range, return an empty list
    if end_index is None:
        return []

    # Return the list of all positive integers from index 42 to index 87, both exclusive

    return my_list[start_index:end_index]
