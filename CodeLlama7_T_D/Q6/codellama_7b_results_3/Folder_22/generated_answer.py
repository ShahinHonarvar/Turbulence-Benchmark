
def all_neg_ints_exclusive(my_list):
    # Define the start and end indices of the range
    start = 40
    end = 200
    # Create an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from the start index to the end index, exclusive
    for i in range(start, end):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the neg_ints list
            neg_ints.append(my_list[i])
    # Return the neg_ints list
    return neg_ints
