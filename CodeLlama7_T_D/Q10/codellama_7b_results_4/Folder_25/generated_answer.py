
def all_odd_ints_exclusive(my_list):
    # Define the start and end indices of the range
    start = 41
    end = 69
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from the start index to the end index, exclusive
    for i in range(start, end):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 41 to index 69, both exclusive
    return odd_ints
