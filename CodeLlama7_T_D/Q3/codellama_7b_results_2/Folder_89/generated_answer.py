
def all_pos_ints_inclusive(my_list):
    # Get the range of indices for positive integers
    start = next((i for i, x in enumerate(my_list) if x > 0), None)
    end = next((i for i, x in enumerate(my_list) if x > 0), None)
    # Check if any positive integers exist within the range
    if start is not None and end is not None:
        # Return the list of all positive integers within the range
        return [x for x in my_list[start:end+1] if x > 0]
    else:
        # If no positive integers exist within the range, return an empty list
        return []
