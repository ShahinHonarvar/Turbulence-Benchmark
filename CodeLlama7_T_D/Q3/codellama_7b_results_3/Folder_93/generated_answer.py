
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the list of integers starting from index 75
    for i in range(75, len(my_list)):

        # Check if the current element is a positive integer
        if my_list[i] > 0:

            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 75 to index 94, both inclusive
    return pos_ints
