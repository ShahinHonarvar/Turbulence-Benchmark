
def all_pos_ints_inclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # If no positive integers exist in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last positive integer in the list

    last_pos_int = next(reversed(my_list)).index(x) for x in reversed(my_list) if x > 0), None)
    # If no positive integers exist in the list, return an empty list
    if last_pos_int is None:
        return []

    # Return the list of all positive integers from index 42 to index 68, both inclusive

    return my_list[first_pos_int:last_pos_int+1]
