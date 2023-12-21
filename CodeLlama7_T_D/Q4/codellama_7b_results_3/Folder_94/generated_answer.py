
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_positive = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # If no positive integers exist in the specified range, return an empty list
    if first_positive is None:
        return []

    # Return the list of all positive integers from index 28 to index 53, both exclusive
    return [x for i, x in enumerate(my_list) if first_positive <= i < first_positive + 10]
