
def all_pos_ints_inclusive(my_list):
    # Get the length of the list
    list_length = len(my_list)
    # Create an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list from index 17 to 78, both inclusive
    for i in range(17, list_length):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the current element to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
