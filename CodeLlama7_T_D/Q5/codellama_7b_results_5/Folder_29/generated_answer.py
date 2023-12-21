
def all_neg_ints_inclusive(my_list):
    # Get the starting and ending indices of the range
    start = 59
    end = 97
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate over the list from the starting index to the ending index
    for i in range(start, end + 1):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the negative integer to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of negative integers
    return neg_ints
