
def all_neg_ints_inclusive(my_list):
    # Get the start and end indices for the range of negative integers
    start = 70
    end = 200
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list, starting from the specified index
    for i in range(start, end + 1):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from the specified range
    return neg_ints
