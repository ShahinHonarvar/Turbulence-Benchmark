
def all_pos_ints_exclusive(my_list):
    # Get the indices of the first and last positive integers in the list
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    last_pos_int = next((i for i, x in enumerate(my_list) if x > 0))

    # Return the list of all positive integers from index first_pos_int to index last_pos_int, both exclusive
    return my_list[first_pos_int:last_pos_int]
