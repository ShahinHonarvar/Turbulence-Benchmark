
def all_neg_ints_inclusive(my_list):
    # Define a range of indices to check for negative integers
    start_index = 56
    end_index = 66
    # Initialize an empty list to store the negative integers found in the range
    neg_ints = []
    # Iterate over the specified range of indices
    for i in range(start_index, end_index + 1):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the negative integer to the list of negative integers found
            neg_ints.append(my_list[i])
    # Return the list of all negative integers found in the specified range, or an empty list if no such integers exist
    return neg_ints
