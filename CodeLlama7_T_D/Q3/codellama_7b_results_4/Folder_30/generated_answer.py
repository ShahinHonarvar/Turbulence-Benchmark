
def all_pos_ints_inclusive(my_list):
    # Get the start and end indices of the range
    start = 55
    end = 98
    # Create an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list from the start index to the end index
    for i in range(start, end+1):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 55 to index 98, both inclusive
    return pos_ints
