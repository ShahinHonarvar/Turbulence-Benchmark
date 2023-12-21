
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate over the specified range of indices in my_list
    for i in range(1, len(my_list)):
        # Check if the current element is negative and add it to the list of negative integers if so
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 1 to index 7, both exclusive
    return neg_ints
