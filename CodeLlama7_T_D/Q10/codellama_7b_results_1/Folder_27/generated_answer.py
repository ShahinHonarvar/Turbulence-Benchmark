
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list, starting from index 28 (inclusive) and ending at index 49 (exclusive)
    for i in range(27, 49):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers in the specified range, or an empty list if no such integers exist
    return odd_ints
