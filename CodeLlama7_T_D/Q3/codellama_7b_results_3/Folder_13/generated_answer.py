
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the list of integers from index 25 to index 87, both inclusive
    for i in range(25, 87 + 1):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 25 to index 87, both inclusive
    return pos_ints
