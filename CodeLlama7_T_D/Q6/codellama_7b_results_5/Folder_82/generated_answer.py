
def all_neg_ints_exclusive(my_list):
    # Find the index of the first negative integer in the list
    first_negative_index = next((i for i, x in enumerate(my_list) if x < 0), None)
    # If there are no negative integers in the list, return an empty list
    if first_negative_index is None:
        return []

    # Find the index of the last negative integer in the list
    last_negative_index = next((i for i, x in enumerate(my_list[first_negative_index:]) if x < 0), None)
    # If there are no negative integers in the specified range, return an empty list
    if last_negative_index is None:
        return []

    # Return the list of all negative integers from index 20 to index 200, both exclusive
    return my_list[first_negative_index:last_negative_index]
