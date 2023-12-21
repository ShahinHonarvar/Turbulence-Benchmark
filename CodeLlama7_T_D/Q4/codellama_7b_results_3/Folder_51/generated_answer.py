
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = None
    for i in range(len(my_list)):
        if my_list[i] > 0:
            first_pos_int = i
            break

    # If there are no positive integers in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last positive integer in the list
    last_pos_int = None
    for i in range(len(my_list))-1, -1):
        if my_list[i] > 0:
            last_pos_int = i
            break

    # If there are no positive integers in the list, return an empty list
    if last_pos_int is None:
        return []

    # Return the list of all positive integers from index 6 to index 9, both exclusive
    return my_list[first_pos_int+6:last_pos_int+9]
