
def all_odd_ints_exclusive(my_list):
    # Get the start and end indices of the range
    start = 44
    end = 67
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list from the start to the end index, exclusive
    for i in range(start, end):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is an odd integer, append it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 44 to index 67, both exclusive
    return odd_ints
