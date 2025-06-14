
def all_pos_ints_inclusive(my_list):
    # Find the index of the first positive integer in the list
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # If no positive integers exist in the specified range, return an empty list
    if first_pos_int is None:
        return []

    # Find the index of the last positive integer in the list

    last_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # If no positive integers exist in the specified range, return an empty list
    if last_pos_int is None:
        return []

    # Return a list of all positive integers from index 70 to index 84, both inclusive
    return [x for x in my_list[first_pos_int:last_pos_int+1] if x > 0]
