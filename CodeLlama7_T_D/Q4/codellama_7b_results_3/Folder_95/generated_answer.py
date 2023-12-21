
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((x for x in my_list if x > 0), None)
    # If no positive integers exist in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last index of the specified range
    last_index = my_list.index(first_pos_int) + 24
    # Return the list of all positive integers from the specified range, exclusive
    return [x for x in my_list[last_index:81] if x > 0]
