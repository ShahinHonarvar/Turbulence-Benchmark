
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list, starting at index 74 and ending at index 95 (both inclusive)
    for i in range(74, 96):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers in the specified range, or an empty list if no such integers exist
    return odd_ints
