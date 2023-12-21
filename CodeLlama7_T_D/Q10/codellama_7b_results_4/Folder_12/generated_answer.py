
def all_odd_ints_exclusive(my_list):
    # Find the starting and ending indices of the range
    start_index = 23
    end_index = 45
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list, starting from the starting index
    for i in range(start_index, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers in the specified range
    return odd_ints
