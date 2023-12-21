
def all_pos_ints_inclusive(my_list):
    # find the first positive integer in the list
    first_pos_int = next((x for x in my_list if x > 0), None)
    # if there are no positive integers in the list, return an empty list
    if first_pos_int is None:
        return []

    # find the last positive integer in the list

    last_pos_int = next(reversed(my_list), None)

    # if there are no positive integers in the list, return an empty list
    if last_pos_int is None:
        return []

    # find the starting index of the first positive integer in the list
    start_index = my_list.index(first_pos_int)

    # find the ending index of the last positive integer in the list
    end_index = my_list.index(last_pos_int) + 1

    # return the list of all positive integers from the starting index to the ending index, inclusive
    return [x for x in my_list[start_index:end_index] if x > 0]
