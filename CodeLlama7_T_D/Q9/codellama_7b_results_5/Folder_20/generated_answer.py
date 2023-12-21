
def all_odd_ints_inclusive(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate over the list from index 56 to index 66 (inclusive)
    for i in range(56, 67):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 56 to index 66 (inclusive), or an empty list if no such integers exist in the input list
    return odd_ints
