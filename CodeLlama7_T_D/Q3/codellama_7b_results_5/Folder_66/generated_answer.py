
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the specified range of the input list
    for i in range(50, 54+1):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the current element to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 50 to index 54, both inclusive
    return pos_ints
