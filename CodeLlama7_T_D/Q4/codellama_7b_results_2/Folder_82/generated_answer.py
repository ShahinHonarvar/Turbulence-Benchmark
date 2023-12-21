
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    for i, x in enumerate(my_list):
        if x > 0:
            start_index = i
            break

    # Find the last positive integer in the list

    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > 0:
            end_index = i
            break

    # Return the list of all positive integers from start to end index, exclusive

    return my_list[start_index + 1:end_index]
