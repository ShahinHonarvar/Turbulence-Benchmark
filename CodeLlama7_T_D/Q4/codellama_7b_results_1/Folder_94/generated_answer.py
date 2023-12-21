
def all_pos_ints_exclusive(my_list):
    # Get the indices of the first and last positive integers
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    last_pos_int = next((i for i, x in enumerate(my_list) if x > 0)) - 1
    # Return the list of positive integers from index 28 to index 53, both exclusive
    return my_list[first_pos_int:last_pos_int]
