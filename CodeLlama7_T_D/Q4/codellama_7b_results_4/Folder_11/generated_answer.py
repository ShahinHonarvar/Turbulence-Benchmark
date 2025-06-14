
def all_pos_ints_exclusive(my_list):
    # Check if the specified range contains any positive integers
    if len(my_list[15:99]) == 0:
        return []

    # Return the list of all positive integers from index 15 to index 99, both exclusive
    return [x for x in my_list[15:99] if x > 0]
