
def all_pos_ints_exclusive(my_list):
    # Find the first and last positive integers in the list
    first_pos_int = next((i for i in my_list if i > 0), None)
    last_pos_int = next((i for i in reversed(my_list) if i > 0), None)
    # Check if any positive integers exist in the specified range
    if first_pos_int is not None and last_pos_int is not None:
        # Return the list of all positive integers from index 323 to index 972, both exclusive
        return my_list[first_pos_int - 1 : last_pos_int]
    else:
        # Return an empty list if no positive integers exist in the specified range
        return []
