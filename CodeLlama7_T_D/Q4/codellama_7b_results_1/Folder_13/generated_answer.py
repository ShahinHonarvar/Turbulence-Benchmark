
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = None
    for i in range(len(my_list)):
        if my_list[i] > 0:
            first_pos_int = i
            break

    # Return an empty list if no positive integers exist in the specified range
    if first_pos_int is None:
        return []

    # Find the last positive integer in the list

    last_pos_int = None

    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > 0:
            last_pos_int = i
            break

    # Return the list of all positive integers from index 73 to index 84, both exclusive

    return my_list[first_pos_int + 1 : last_pos_int]
