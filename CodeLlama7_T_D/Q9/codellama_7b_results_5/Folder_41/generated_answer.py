
def all_odd_ints_inclusive(my_list):
    # Get the starting and ending indices of the specified range
    start_index = 6
    end_index = 6
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the specified range of the input list
    for i in range(start_index, end_index + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from the specified range, or an empty list if no such integers exist
    return odd_ints
