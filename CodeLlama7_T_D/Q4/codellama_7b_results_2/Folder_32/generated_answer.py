
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((x for x in my_list if x > 0), None)
    # If no positive integers exist in the specified range, return an empty list
    if first_pos_int is None:
        return []

    # Find the last positive integer in the list

    last_pos_int = next((x for x in my_list[::-1] if x > 0), None)

    # Create a slice of the list with all positive integers from index 11 to index 76, both exclusive

    pos_ints_slice = my_list[first_pos_int - 1: last_pos_int + 1]

    # Return the list of all positive integers in the specified range

    return pos_ints_slice
