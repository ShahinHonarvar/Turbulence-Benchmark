
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is positive and store it in a temporary variable
        temp = my_list[i]
        if temp > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(temp)
    # Return the list of all positive integers from index 533 to index 605, both inclusive
    return pos_ints[533:605]
