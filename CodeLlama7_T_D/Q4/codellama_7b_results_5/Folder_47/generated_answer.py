
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((x for x in my_list if x > 0), None)
    # If no positive integers exist in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last positive integer in the list

    last_pos_int = next((x for x in my_list[::-1] if x > 0), None)

    # Return the list of all positive integers from index 64 to index 80, both exclusive

    return [x for x in my_list[63:81] if x > 0]
