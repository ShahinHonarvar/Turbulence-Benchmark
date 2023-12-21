
def all_pos_ints_inclusive(my_list):
    # Find the index of the first positive integer in the list
    start_index = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # If no positive integers exist in the specified range, return an empty list
    if start_index is None:
        return []

    # Find the index of the last positive integer in the list

    end_index = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # If no positive integers exist in the specified range, return an empty list
    if end_index is None:
        return []

    # Return the list of all positive integers from index start_index to index end_index, both inclusive

    return [x for x in my_list[start_index:end_index+1] if x > 0]
