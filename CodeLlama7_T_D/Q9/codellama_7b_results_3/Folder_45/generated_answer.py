 def all_odd_ints_inclusive(my_list):
    # Define the start and end indices of the range
    start = 30
    end = 200
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the range of indices
    for i in range(start, end + 1):
        # Check if the current index is odd
        if my_list[i] % 2 != 0:
            # If it is odd, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers in the specified range
    return odd_ints
