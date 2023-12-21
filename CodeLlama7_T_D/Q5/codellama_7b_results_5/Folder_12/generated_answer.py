
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 14 to index 64, both inclusive
    for i in range(14, 65):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, append it to the list of negative integers
            neg_ints.append(my_list[i])
    return neg_ints
