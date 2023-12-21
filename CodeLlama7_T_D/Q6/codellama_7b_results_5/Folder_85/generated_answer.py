
def all_neg_ints_exclusive(my_list):
    # Get the index of the first negative integer
    first_negative_index = next((i for i, x in enumerate(my_list) if x < 0)), None)
    # If there are no negative integers in the list, return an empty list
    if first_negative_index is None:
        return []

    # Get the index of the last negative integer

    last_negative_index = next((i for i, x in enumerate(my_list) if x < 0)), None)


    # Return the list of all negative integers from the first to the last, exclusive

    return my_list[first_negative_index + 1:last_negative_index]
