
def all_odd_ints_exclusive(my_list):
    # Define the start and end indices for the range of odd integers
    start = 68
    end = 99
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from the start index to the end index
    for i in range(start, end + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is an odd integer, append it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 68 to index 99, both exclusive
    return odd_ints
