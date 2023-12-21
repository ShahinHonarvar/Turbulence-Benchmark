
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list of integers, starting at index 87 and ending at index 95 (exclusive)
    for i in range(87, 95):
        # Check if the current integer is an odd number
        if my_list[i] % 2 != 0:
            # If it is an odd number, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 87 to index 95 (exclusive)
    return odd_ints
