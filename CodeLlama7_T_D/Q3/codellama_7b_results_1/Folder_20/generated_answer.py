
def all_pos_ints_inclusive(my_list):
    # Define the range of indices
    start_index = 56
    end_index = 66
    # Create an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers
    for i in range(start_index, end_index + 1):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
