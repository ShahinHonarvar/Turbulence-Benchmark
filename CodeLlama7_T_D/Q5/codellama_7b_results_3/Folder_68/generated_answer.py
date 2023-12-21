
def all_neg_ints_inclusive(my_list):
    # Create an empty list to store the negative integers
    neg_ints = []

    # Loop through the input list and append any negative integers to the output list
    for i in range(len(my_list)):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 0 to index 8, both inclusive
    return neg_ints
