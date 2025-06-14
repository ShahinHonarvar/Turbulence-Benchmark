
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers starting from index 62 and ending at index 92, both inclusive
    for i in range(62, 93):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is a positive integer, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 62 to index 92, both inclusive
    return pos_ints
