
def all_pos_ints_inclusive(my_list):
    # Find the index of the first positive integer
    first_pos_int = next((i for i, x in enumerate(my_list) if x > 0)), None)
    # Find the index of the last positive integer
    last_pos_int = next((i for i, x in enumerate(my_list[::-1]) if x > 0)), None)
    # Return the list of all positive integers from first to last index, inclusive
    return [x for x in my_list[first_pos_int:last_pos_int+1] if x > 0]
