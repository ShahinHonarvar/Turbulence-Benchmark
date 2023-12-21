
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list of integers
    for i in range(100, 101):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # If it is odd, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 100 to index 101, both exclusive
    return odd_ints
