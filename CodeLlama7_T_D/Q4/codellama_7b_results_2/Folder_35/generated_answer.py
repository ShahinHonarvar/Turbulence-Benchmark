
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_positive = next((i for i in my_list if i > 0), None)
    # If no positive integers exist in the specified range, return an empty list
    if first_positive is None:
        return []

    # Find the last positive integer in the list

    last_positive = next(reversed(my_list), None)

    # Return the list of all positive integers from index 10 to index 79, both exclusive

    return [i for i in my_list[10:80] if i > 0]
