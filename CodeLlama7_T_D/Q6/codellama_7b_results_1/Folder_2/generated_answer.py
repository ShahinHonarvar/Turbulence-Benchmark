
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer index
    first_negative_index = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If no negative integers exist in the list, return an empty list
    if first_negative_index is None:
        return []

    # Find the last negative integer index
    last_negative_index = next((i for i, x in enumerate(my_list[first_negative_index:]) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if last_negative_index is None:
        return []

    # Return the list of all negative integers from index 36 to index 52, both exclusive
    return my_list[first_negative_index + 36: first_negative_index + 52]
