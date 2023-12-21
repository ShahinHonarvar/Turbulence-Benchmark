
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list of integers
    for i in range(len(my_list)):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
