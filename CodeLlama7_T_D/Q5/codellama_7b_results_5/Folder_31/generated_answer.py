
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list starting from index 75
    for i in range(75, len(my_list)):
        # Check if the current element is negative
        if my_list[i] < 0:
            # If it is negative, append it to the neg_ints list
            neg_ints.append(my_list[i])
    # Return the neg_ints list
    return neg_ints
