
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((x for x in my_list if x > 0), None)
    # If there are no positive integers in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the index of the first positive integer in the list
    first_pos_int_index = my_list.index(first_pos_int)
    # Return the list of all positive integers from index 20 to index 36, both exclusive
    return my_list[first_pos_int_index + 1:first_pos_int_index + 17]
