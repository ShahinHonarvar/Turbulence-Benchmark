
def all_odd_ints_exclusive(my_list):
    # Define start and end indices for the range of odd integers
    start = 20
    end = 35
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list from the defined start index to the defined end index, exclusive
    for i in range(start, end):
        # Check if the current index is odd and not equal to the start index (to avoid duplicates)
        if my_list[i] % 2 != 0 and i != start:
            # If it is odd, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 20 to index 35, exclusive
    return odd_ints
