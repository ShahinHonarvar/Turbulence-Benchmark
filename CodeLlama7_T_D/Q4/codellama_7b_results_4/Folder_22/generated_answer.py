
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers from index 40 to index 200 (both exclusive)
    for i in range(40, 201):
        # If the current element is a positive integer, append it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 40 to index 200 (both exclusive)
    return pos_ints
