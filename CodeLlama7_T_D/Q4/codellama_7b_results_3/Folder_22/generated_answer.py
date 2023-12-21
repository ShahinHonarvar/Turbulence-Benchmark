
def all_pos_ints_exclusive(my_list):
    # Get the indices of the first and last positive integers
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    last_pos_int = next((i for i, x in enumerate(my_list) if x > 0)) - 1)
    # Check if there are any positive integers in the specified range
    if first_pos_int is not None and last_pos_int is not None:
        # Return the list of all positive integers from index 40 to index 200, both exclusive
        return my_list[first_pos_int:last_pos_int]
    else:
        # If no positive integers exist in the specified range, return an empty list
        return []
