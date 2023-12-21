
def all_pos_ints_inclusive(my_list):
    # Find the starting and ending indices of the positive integers in the list
    start = None
    end = None
    for i, x in enumerate(my_list):
        if x > 0:
            if start is None:
                start = i
            end = i

    # Return an empty list if no positive integers exist in the specified range
    if start is None:
        return []

    # Return the list of all positive integers from index 209 to index 556, both inclusive
    return my_list[start:end+1]
