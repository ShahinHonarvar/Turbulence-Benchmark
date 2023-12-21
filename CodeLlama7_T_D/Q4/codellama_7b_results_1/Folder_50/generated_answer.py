
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the range
    first_pos_int = next((i for i in my_list if i > 0), None)
    # If no positive integers exist in the range, return an empty list
    if first_pos_int is None:
        return []

    # Find the last positive integer in the range

    last_pos_int = next((i for i in my_list[70:] if i > 0), None)
    # If no positive integers exist in the range, return an empty list
    if last_pos_int is None:
        return []

    # Return the list of all positive integers from index 70 to index 98, both exclusive
    return my_list[70:last_pos_int + 1]
