
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the specified range of indices in the list
    for i in range(90, 201):
        # If the current element is an odd integer, add it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # Return the list of all odd integers in the specified range, or an empty list if no odd integers exist
    return odd_ints
