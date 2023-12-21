
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the list of integers, starting at index 661
    for i in range(661, len(my_list)):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 661 to index 924, both inclusive
    return pos_ints
