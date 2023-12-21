
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate over the specified range of indices in my_list
    for i in range(8, 10):

        # Check if the current element is a negative integer
        if my_list[i] < 0:

            # If it is, add it to the neg_ints list
            neg_ints.append(my_list[i])

    # Return the list of all negative integers found in the specified range, or an empty list if no such integers exist
    return neg_ints
