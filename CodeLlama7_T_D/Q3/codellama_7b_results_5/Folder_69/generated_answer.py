
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is positive
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 32 to index 35, both inclusive
    return pos_ints
