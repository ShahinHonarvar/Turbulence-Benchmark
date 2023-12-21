
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list from index 37 to 76 (both inclusive)
    for i in range(37, 77):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 37 to index 76 (both inclusive), or an empty list if no positive integers exist in the specified range
    return pos_ints
