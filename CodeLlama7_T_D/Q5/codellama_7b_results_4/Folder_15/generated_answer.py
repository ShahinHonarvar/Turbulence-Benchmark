
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of indices in my_list
    for i in range(len(my_list)):

        # Check if the current element is a negative integer
        if my_list[i] < 0:

            # Add the negative integer to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 0 to index 3, both inclusive
    return neg_ints
