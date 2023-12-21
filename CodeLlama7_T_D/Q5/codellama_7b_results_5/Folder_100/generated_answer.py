
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list starting from index 42
    for i in range(42, len(my_list)):
        # Check if the current element is negative
        if my_list[i] < 0:
            # Add the current element to the list of negative integers
            neg_ints.append(my_list[i])
    return neg_ints
