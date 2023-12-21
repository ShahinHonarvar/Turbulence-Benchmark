
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((i for i in my_list if i > 0), None)
    # If no positive integers exist in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last index of the specified range

    last_index = min(len(my_list), 52) - 1

    # Return the list of all positive integers from index 36 to index 52, both exclusive

    return [i for i in my_list[36:last_index] if i > 0]
