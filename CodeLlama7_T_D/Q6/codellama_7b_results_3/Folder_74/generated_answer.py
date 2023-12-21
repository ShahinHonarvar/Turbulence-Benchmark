
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list and append any negative integers to the 'neg_ints' list
    for i in range(13, 70):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the 'neg_ints' list
    return neg_ints
