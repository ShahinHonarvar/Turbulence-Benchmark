
def all_neg_ints_exclusive(my_list):
    # Find the index of the first negative integer
    first_neg_index = next((i for i, x in enumerate(my_list) if x < 0)), None)
    # If no negative integers exist in the list, return an empty list
    if first_neg_index is None:
        return []

    # Find the index of the last negative integer

    last_neg_index = next((i for i, x in enumerate(my_list[first_neg_index:]) if x < 0), None)
    # If no negative integers exist in the specified range, return an empty list
    if last_neg_index is None:
        return []

    # Return the list of all negative integers from index 598 to index 767, both exclusive

    return my_list[first_neg_index:last_neg_index+1]
