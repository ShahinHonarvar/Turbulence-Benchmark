
def all_pos_ints_inclusive(my_list):
    # Find the starting and ending indices of the positive integers in the list
    start_idx = None
    end_idx = None
    for i in range(len(my_list)):
        if my_list[i] > 0:
            # If we haven't found the starting index yet, set it to this index
            if start_idx is None:
                start_idx = i

            # Set the ending index to this index
            end_idx = i

    # Return an empty list if no positive integers were found in the specified range
    if start_idx is None:
        return []

    # Return the list of all positive integers from the starting to ending indices, inclusive
    return [my_list[i] for i in range(start_idx, end_idx+1)]
