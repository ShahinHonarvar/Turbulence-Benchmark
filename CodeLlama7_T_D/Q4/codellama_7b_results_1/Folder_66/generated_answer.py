
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_positive = next((i for i in my_list if i > 0), None)
    # If no positive integers exist in the list, return an empty list
    if first_positive is None:
        return []

    # Find the last positive integer in the list

    last_positive = next((i for i in my_list[::-1] if i > 0), None)
    # If no positive integers exist in the list, return an empty list
    if last_positive is None:
        return []

    # Return the list of all positive integers from index 13 to index 76, both exclusive

    return my_list[first_positive - 1 : last_positive]
