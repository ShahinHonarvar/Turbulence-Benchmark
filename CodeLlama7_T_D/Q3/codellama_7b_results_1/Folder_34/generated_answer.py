
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers, starting from index 60 and ending at index 200 (both inclusive)
    for i in range(60, 201):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is a positive integer, append it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 60 to index 200 (both inclusive), or an empty list if no positive integers exist in the specified range
    return pos_ints
