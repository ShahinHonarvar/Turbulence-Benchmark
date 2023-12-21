
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the list of integers and check if each element is a positive integer
    for i in range(2, len(my_list)):
        if my_list[i] > 0:
            # If the element is a positive integer, add it to the list of positive integers
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 2 to index 8, both exclusive
    return pos_ints
