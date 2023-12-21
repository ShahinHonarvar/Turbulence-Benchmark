
def all_pos_ints_exclusive(my_list):
    # Find the first and last positive integers in the list
    first_pos_int = next((x for x in my_list if x > 0), None)
    last_pos_int = next((x for x in reversed(my_list) if x > 0), None)
    # Check if there are any positive integers in the specified range
    if first_pos_int is not None and last_pos_int is not None:
        # Return the list of all positive integers from index 48 to index 74, both exclusive
        return my_list[my_list.index(first_pos_int):my_list.index(last_pos_int)]
    else:
        # If no positive integers exist in the specified range, return an empty list
        return []
