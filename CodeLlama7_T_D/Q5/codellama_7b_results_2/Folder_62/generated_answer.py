
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(91, 100):

        # Check if the current element is a negative integer
        if my_list[i] < 0:

            # Add the negative integer to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from the specified range, or an empty list if no such integers exist
    return neg_ints
