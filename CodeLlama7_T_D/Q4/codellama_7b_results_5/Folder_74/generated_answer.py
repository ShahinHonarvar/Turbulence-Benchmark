
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = None
    for i in range(13, len(my_list)):
        if my_list[i] > 0:
            first_pos_int = my_list[i]
            break

    # Find the last positive integer in the list
    last_pos_int = None
    for i in range(len(my_list) - 1, 13, -1):
        if my_list[i] > 0:
            last_pos_int = my_list[i]
            break

    # Return the list of all positive integers from index 13 to index 70, both exclusive
    return [my_list[i] for i in range(13, len(my_list)) if my_list[i] > 0 and (first_pos_int is None or first_pos_int <= my_list[i]) and (last_pos_int is None or last_pos_int >= my_list[i])]
