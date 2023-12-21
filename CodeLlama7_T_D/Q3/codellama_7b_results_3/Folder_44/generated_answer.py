
def all_pos_ints_inclusive(my_list):
    # Find the start and end indices of the positive integers in the list
    start_index = next((i for i, x in enumerate(my_list) if x > 0), None)
    end_index = next((i for i, x in enumerate(my_list) if x < 0], None)
    # Return an empty list if no positive integers exist in the specified range
    if start_index is None or end_index is None:
        return []

    # Return a list of all positive integers from index 13 to index 68, both inclusive
    return [x for x in my_list[start_index:end_index + 1] if x > 0]
