
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers, starting from index 31
    for i in range(31, len(my_list)):
        # Check if the current integer is positive
        if my_list[i] > 0:
            # If it is positive, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 31 to index 34, both inclusive
    return pos_ints
