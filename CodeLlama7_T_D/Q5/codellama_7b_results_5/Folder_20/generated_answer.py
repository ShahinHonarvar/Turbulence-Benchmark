
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list and append each negative integer to the neg_ints list
    for i in range(56, 67):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
