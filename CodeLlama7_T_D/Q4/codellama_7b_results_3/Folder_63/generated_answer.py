
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the range
    first_pos_int = None
    for i in range(38, 52):
        if my_list[i] > 0:
            first_pos_int = my_list[i]
            break

    # If no positive integers exist in the range, return an empty list
    if first_pos_int is None:
        return []

    # Return the list of all positive integers from index 38 to index 52, both exclusive
    return [my_list[i] for i in range(38, 52) if my_list[i] > 0 and my_list[i] != first_pos_int]
