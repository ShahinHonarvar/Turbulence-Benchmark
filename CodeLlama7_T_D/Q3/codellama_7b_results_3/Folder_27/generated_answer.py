
def all_pos_ints_inclusive(my_list):
    # Get the start and end indices of the range
    start = 66
    end = 93
    # Check if there are any positive integers in the specified range
    if not any(x > 0 for x in my_list[start:end+1])):
        return []

    # Return the list of all positive integers from index start to index end, both inclusive
    return [x for x in my_list[start:end+1] if x > 0]
