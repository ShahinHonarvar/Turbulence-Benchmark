
def all_pos_ints_inclusive(my_list):
    # Check if there are any positive integers in the specified range
    if not any(my_list[10:100] > 0):
        return []

    # Return the list of all positive integers from index 10 to index 100, both inclusive
    return [x for x in my_list[10:100] if x > 0]
