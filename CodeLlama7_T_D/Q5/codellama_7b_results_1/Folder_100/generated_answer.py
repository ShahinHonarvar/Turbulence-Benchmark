
def all_neg_ints_inclusive(my_list):
    # Get the indices of the first and last negative integers in the list
    first_negative_index = next((i for i, x in enumerate(my_list) if x < 0), None)
    last_negative_index = next((i for i, x in enumerate(my_list[::-1]) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if first_negative_index is None or last_negative_index is None:
        return []

    # Return the list of all negative integers from index 42 to index 68, both inclusive
    return my_list[first_negative_index:last_negative_index+1]
