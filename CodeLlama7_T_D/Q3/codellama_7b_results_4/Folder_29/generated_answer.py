
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list from index 59 to index 97, both inclusive
    for i in range(59, 98):
        # If the current element is a positive integer, add it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
