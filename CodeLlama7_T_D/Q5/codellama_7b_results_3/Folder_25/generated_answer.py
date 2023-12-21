
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate over the list and check if each element is negative
    for i in range(29, 93 + 1):
        if my_list[i] < 0:
            # If the element is negative, append it to the list of negative integers
            neg_ints.append(my_list[i])
    return neg_ints
