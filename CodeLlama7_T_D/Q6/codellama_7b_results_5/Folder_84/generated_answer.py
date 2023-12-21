
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer index
    first_negative_index = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_negative_index is None:
        return []

    # Find the last negative integer index

    last_negative_index = next(reversed(range(first_negative_index, len(my_list)))) + 1)

    # Return the list of all negative integers from the specified range

    return [my_list[i] for i in range(first_negative_index, last_negative_index)]
