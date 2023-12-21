
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list starting from index 20
    for i in range(20, len(my_list)):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the current element to the list of negative integers
            neg_ints.append(my_list[i])
    return neg_ints
