
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the list of integers from index 12 to index 92, both inclusive
    for i in range(12, 93):

        # Check if the current element is a positive integer

        if my_list[i] > 0:

            # If it is, add it to the list of positive integers

            pos_ints.append(my_list[i])

    # Return the list of all positive integers in the specified range, or an empty list if no such integers exist

    return pos_ints
