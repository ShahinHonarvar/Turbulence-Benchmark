
def all_pos_ints_inclusive(my_list):
    # Check if the specified range contains any positive integers
    if not any(x > 0 for x in my_list[34:56]):
        return []

    # Return the list of all positive integers from index 34 to index 55, both inclusive
    return [x for x in my_list[34:56] if x > 0]
