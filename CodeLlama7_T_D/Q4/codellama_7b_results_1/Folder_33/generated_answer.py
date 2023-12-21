
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers
    for i in range(len(my_list)):
        # If the current integer is positive and not at index 369 or 983, add it to the list of positive integers
        if my_list[i] > 0 and i != 369 and i != 983:
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 369 to index 983, both exclusive
    return pos_ints
