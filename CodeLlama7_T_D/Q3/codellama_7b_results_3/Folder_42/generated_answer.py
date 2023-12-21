
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers from index 29 to 79, both inclusive
    for i in range(29, 80):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the current element to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
