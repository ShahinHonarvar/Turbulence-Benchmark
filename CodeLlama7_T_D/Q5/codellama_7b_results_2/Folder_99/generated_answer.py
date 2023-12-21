
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list from index 310 to index 370, both inclusive
    for i in range(310, 371):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, append it to the neg_ints list
            neg_ints.append(my_list[i])

    # Return the neg_ints list
    return neg_ints
