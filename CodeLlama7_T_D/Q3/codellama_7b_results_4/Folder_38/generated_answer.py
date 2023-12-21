
def all_pos_ints_inclusive(my_list):
    # Find the first positive integer in the list
    first_pos_int = next((i for i in my_list if i > 0), None)
    # If there are no positive integers in the list, return an empty list
    if first_pos_int is None:
        return []

    # Find the last positive integer in the list

    last_pos_int = next((i for i in reversed(my_list) if i > 0), None)

    # Return the list of all positive integers from index 22 to index 63, both inclusive

    return my_list[first_pos_int - 1 : last_pos_int + 1]
