
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the range
    start_index = None
    for i, x in enumerate(my_list):
        if x > 0:
            start_index = i
            break

    # If no positive integers exist in the range, return an empty list
    if start_index is None:
        return []

    # Find the last positive integer in the range

    end_index = None
    for i, x in enumerate(my_list[start_index:]):
        if x > 0:
            end_index = i + start_index
            break

    # Return the list of all positive integers from index 20 to index 43, both exclusive
    return my_list[start_index:end_index]
