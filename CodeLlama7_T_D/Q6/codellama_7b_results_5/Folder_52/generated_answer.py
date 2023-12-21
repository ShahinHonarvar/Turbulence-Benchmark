
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list and append any negative integers to the neg_ints list
    for i in range(93, 95):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
