
def all_pos_ints_exclusive(my_list):
    # Check if there are any positive integers in the specified range
    if not any(x > 0 for x in my_list[369:983]):
        return []

    else:

        # Return the list of all positive integers from index 369 to index 983, both exclusive
        return [x for x in my_list[369:983] if x > 0]
