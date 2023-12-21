
def all_neg_ints_inclusive(my_list):
    # Create a new list to store the negative integers
    neg_ints = []
    # Iterate through the list and append any negative integers to the new list
    for i in range(50, 55):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
