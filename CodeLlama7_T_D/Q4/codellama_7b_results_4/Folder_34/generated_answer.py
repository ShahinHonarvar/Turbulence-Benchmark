
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((x for x in my_list if x > 0), None)
    # If no positive integers exist in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last position of a positive integer in the list
    last_pos_int = len(my_list) - 1
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > 0:
            last_pos_int = i

    # Return the list of all positive integers from index 60 to index 200, both exclusive
    return my_list[last_pos_int + 1: first_pos_int - 1]
