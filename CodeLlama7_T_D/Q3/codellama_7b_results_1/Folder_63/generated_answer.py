
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers starting from index 22 (inclusive) and ending at index 88 (exclusive)
    for i in range(22, 88):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the current element to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
