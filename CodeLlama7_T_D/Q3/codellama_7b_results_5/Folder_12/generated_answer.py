
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers starting from index 14 to index 64, both inclusive
    for i in range(14, 65):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the current element to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 14 to index 64, both inclusive
    return pos_ints
