
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list, if any
    first_positive = next((i for i in my_list if i > 0), None)
    # If no positive integers exist in the specified range, return an empty list
    if first_positive is None:
        return []

    # Find the last positive integer in the list, exclusive of index 51

    last_positive = next((i for i in my_list[20:] if i > 0), None)

    # Return the list of all positive integers from index 20 to index 51, both exclusive

    return my_list[20:last_positive]
